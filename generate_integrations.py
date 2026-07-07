#!/usr/bin/env python3
"""把「工具集成文档」生成为 hao.ai/docs 同款风格（Nextra）的自有站点。

内容策略：只抓取一次，抓来的 Markdown 落在本地 markdown/，作为你自己的
内容源。之后每次生成都从本地 markdown/ 重建站点，不再回原站抓取——
除非你显式加 --fetch 主动更新。

用法:
    python3 generate_integrations.py            # 用本地 markdown/ 生成 docs-site/（不抓取）
    python3 generate_integrations.py --fetch    # 重新从原站抓取一次，刷新本地 markdown/
    python3 generate_integrations.py --dev      # 生成后启动本地预览 (Next.js dev)
    python3 generate_integrations.py --build     # 生成后构建静态站点到 docs-site/out/
    python3 generate_integrations.py --site-name "MyAPI" --site-url "https://api.example.com"

首次运行若本地还没有 markdown/，会自动抓取一次。之后就用你自己的内容。

预览/构建站点需要 Node.js 20+（首次会自动 npm install 到 docs-site/）。

站点品牌可配置（优先级：命令行参数 > site.config.json > 内置默认值）:
    site.config.json 示例: {"site_name": "MyAPI", "site_url": "https://api.example.com"}
    生成时会把内容中所有 HaoAI / HAOAI / haoai / hao.ai / https://hao.ai
    替换为配置的站点名称与站点 URL（含环境变量名、锚点、图片文件名）。

输出结构:
    markdown/
      README.md                  # 目录索引
      zh/index.md                # 中文集成索引（工具总表）
      zh/claude-code/index.md    # 模块概览页
      zh/claude-code/installation.md  # 模块嵌套子页
      en/...                     # 英文，结构与中文一致
      assets/<module>/*.webp     # 图片按模块归类

实现说明: 原站没有公开的 .md 端点，「Copy page」按钮复制的是嵌在页面
React Flight 数据（self.__next_f.push）里的 sourceCode 字段，本脚本直接
解析该字段（含 $ref 文本行引用），拿到与按钮完全一致的原始 MDX，再做
JSX 组件清洗（Cards/Callout 等）、图片本地化、内链重写与品牌替换。

仅依赖 Python 标准库。
"""

import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent

BASE = "https://hao.ai"  # 抓取来源，勿改
LOCALES = ["zh", "en"]
SECTION = "integrations"
OUT = Path(__file__).resolve().parent / "markdown"
CONFIG_FILE = Path(__file__).resolve().parent / "site.config.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) integrations-doc-mirror/2.0"
WORKERS = 8

# 站点品牌配置（由 load_config() 填充）
SITE_NAME = "HaoAI"
SITE_URL = BASE
SITE_HOST = "hao.ai"
NAME_UPPER = "HAOAI"  # 环境变量风格，如 HAOAI_API_KEY
NAME_SLUG = "haoai"   # 锚点/文件名风格，如 why-use-haoai


def load_config(args) -> None:
    """加载站点配置：命令行参数 > site.config.json > 默认值。"""
    global SITE_NAME, SITE_URL, SITE_HOST, NAME_UPPER, NAME_SLUG
    cfg = {"site_name": SITE_NAME, "site_url": SITE_URL}
    if CONFIG_FILE.exists():
        cfg.update(json.loads(CONFIG_FILE.read_text(encoding="utf-8")))
    if args.site_name:
        cfg["site_name"] = args.site_name
    if args.site_url:
        cfg["site_url"] = args.site_url
    SITE_NAME = cfg["site_name"].strip()
    SITE_URL = cfg["site_url"].strip().rstrip("/")
    SITE_HOST = urllib.parse.urlsplit(SITE_URL).netloc or SITE_URL
    NAME_UPPER = re.sub(r"[^A-Z0-9]+", "_", SITE_NAME.upper()).strip("_")
    NAME_SLUG = re.sub(r"[^a-z0-9]+", "-", SITE_NAME.lower()).strip("-")
    print(f"站点配置: 名称={SITE_NAME}  URL={SITE_URL}")


def rebrand(text: str) -> str:
    """把原站品牌（名称/域名/URL）替换为配置的站点品牌。"""
    if SITE_URL == BASE and SITE_NAME == "HaoAI":
        return text
    text = text.replace(BASE, SITE_URL)                        # https://hao.ai
    text = re.sub(r"hao\.ai", SITE_HOST, text, flags=re.I)     # 裸域名/子域名/Hao.ai
    text = text.replace("HAOAI", NAME_UPPER)                   # 环境变量名
    text = text.replace("HaoAI", SITE_NAME)                    # 品牌名
    text = text.replace("haoai", NAME_SLUG)                    # 锚点/文件名
    return text


def fetch(url: str, binary: bool = False, retries: int = 3):
    """带重试的 HTTP GET（自动对非 ASCII 路径做百分号编码）。"""
    parts = urllib.parse.urlsplit(url)
    url = urllib.parse.urlunsplit(
        parts._replace(path=urllib.parse.quote(parts.path, safe="/%"))
    )
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            return data if binary else data.decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(1 + attempt)
    raise RuntimeError(f"下载失败 {url}: {last_err}")


def save(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        path.write_text(data, encoding="utf-8")
    else:
        path.write_bytes(data)


# ---------------------------------------------------------------- MDX 提取

def extract_mdx(page_html: str) -> str | None:
    """从页面的 React Flight 数据中提取原始 MDX（sourceCode 字段）。"""
    parts = re.findall(
        r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)', page_html
    )
    flight = "".join(json.loads('"' + p + '"') for p in parts)
    m = re.search(r'"sourceCode":"((?:[^"\\]|\\.)*)"', flight)
    if not m:
        return None
    val = json.loads('"' + m.group(1) + '"')
    if not re.fullmatch(r"\$[0-9a-f]+", val):
        return val
    # $ref -> 长度定界的文本行 "<id>:T<hex字节长>,<内容>"
    rid = re.escape(val[1:])
    tm = re.search(rf"(?<![0-9a-zA-Z]){rid}:T([0-9a-f]+),", flight)
    if not tm:
        return None
    n = int(tm.group(1), 16)
    return flight[tm.end():].encode("utf-8")[:n].decode("utf-8", "replace")


# ---------------------------------------------------------------- 爬取

def crawl(locale: str) -> dict:
    """BFS 抓取一个语言下 integrations 全部页面，返回 {子路径: mdx}。

    子路径 "" 表示索引页，"claude-code/installation" 表示嵌套子页。
    """
    pages: dict = {}
    frontier = {""}
    seen = {""}
    link_re = re.compile(
        rf"(?<!images)/(?:docs/)?(?:zh|en)/{SECTION}/([a-zA-Z0-9/_-]+)"
    )
    while frontier:
        results = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futs = {
                pool.submit(
                    fetch,
                    f"{BASE}/docs/{locale}/{SECTION}" + (f"/{p}" if p else ""),
                ): p
                for p in frontier
            }
            for fut in concurrent.futures.as_completed(futs):
                p = futs[fut]
                try:
                    results[p] = fut.result()
                except Exception as e:  # noqa: BLE001
                    print(f"  [fail] {locale}/{p or '(index)'}: {e}")
        frontier = set()
        for p, html in results.items():
            mdx = extract_mdx(html)
            if mdx is None:
                print(f"  [warn] {locale}/{p or '(index)'}: 未找到 sourceCode")
                continue
            pages[p] = mdx
            print(f"  [ok] {locale}/{SECTION}/{p or '(index)'} ({len(mdx)}B)")
            for link in link_re.findall(html) + link_re.findall(mdx):
                sub = link.strip("/").split("#")[0].split("?")[0]
                if sub and sub not in seen:
                    seen.add(sub)
                    frontier.add(sub)
    return pages


# ---------------------------------------------------------------- 转换

def md_file_for(path: str, all_paths: set) -> str:
    """页面子路径 -> 输出 .md 相对路径（有子页的用 <dir>/index.md）。"""
    if not path:
        return "index.md"
    if any(other.startswith(path + "/") for other in all_paths):
        return f"{path}/index.md"
    return f"{path}.md"


def module_of(path: str) -> str:
    return path.split("/")[0] if path else "index"


def localize_images(mdx: str, locale: str, page_path: str, md_file: str) -> str:
    """下载 MDX 引用的图片到 assets/<module>/，并把链接改为相对路径。"""

    def repl(m: re.Match) -> str:
        alt, url = m.group(1), m.group(2)
        if not url.startswith("/"):
            return m.group(0)  # 外链图片保持原样
        seg = urllib.parse.urlparse(url).path
        # /docs/images/integrations/<module>/<file> 按图片自身归属分模块
        im = re.match(rf"/docs/images/(?:zh/|en/)?{SECTION}/([^/]+)/", seg)
        module = im.group(1) if im else module_of(page_path)
        name = rebrand(Path(seg).name)
        local = OUT / "assets" / module / name
        if not local.exists():
            try:
                save(local, fetch(BASE + seg, binary=True))
            except Exception as e:  # noqa: BLE001
                print(f"  [warn] 图片下载失败 {seg}: {e}")
                return m.group(0)
        rel = os.path.relpath(local, (OUT / locale / md_file).parent)
        return f"![{alt}]({rel})"

    return re.sub(r"!\[([^\]]*)\]\(([^)\s]+)[^)]*\)", repl, mdx)


def rewrite_md_links(mdx: str, md_file: str, all_paths: set) -> str:
    """内链改写：integrations 内互链 -> 相对 .md 路径；其余 -> 站点绝对地址。"""
    cur_dir = Path(md_file).parent

    def to_rel(sub: str) -> str:
        sub = sub.strip("/")
        anchor = ""
        if "#" in sub:
            sub, anchor = sub.split("#", 1)
            anchor = "#" + anchor
        target = md_file_for(sub, all_paths)
        return os.path.relpath(target, cur_dir) + anchor

    # markdown 链接与 JSX href 里的 /zh/integrations/... 或 /docs/zh/integrations/...
    def integ(m: re.Match) -> str:
        return m.group(1) + to_rel(m.group(2)) + m.group(3)

    mdx = re.sub(
        rf'(\]\(|href=")/(?:docs/)?(?:zh|en)/{SECTION}/([a-zA-Z0-9/_#?-]+)([)"])',
        integ,
        mdx,
    )
    # 指向 integrations 索引页本身
    mdx = re.sub(
        rf'(\]\(|href=")/(?:docs/)?(?:zh|en)/{SECTION}/?([)"])',
        lambda m: m.group(1)
        + os.path.relpath("index.md", cur_dir)
        + m.group(2),
        mdx,
    )
    # 其余站内根相对链接 -> 站点绝对地址（品牌替换前用 BASE，rebrand 会统一改写）
    mdx = re.sub(r'(\]\(|href=")(/[^)"\s]*)', rf"\g<1>{BASE}\g<2>", mdx)
    return mdx


def clean_jsx(mdx: str) -> str:
    """把常见 Nextra JSX 组件降级为纯 Markdown。"""
    # import 语句
    mdx = re.sub(r"^import\s.*$\n?", "", mdx, flags=re.M)
    # <Cards.Card title=".." href=".." /> -> 列表链接
    def card(m: re.Match) -> str:
        attrs = m.group(1)
        t = re.search(r'title="([^"]*)"', attrs)
        h = re.search(r'href="([^"]*)"', attrs)
        if t and h:
            return f"- [{t.group(1)}]({h.group(1)})"
        return ""
    mdx = re.sub(r"<Cards\.Card\s+([^>]*?)/>", card, mdx)
    mdx = re.sub(r"^[ \t]*</?Cards>[ \t]*$\n?", "", mdx, flags=re.M)
    # <Callout type="..."> ... </Callout> -> 引用块
    marks = {"warning": "⚠️", "error": "🚫", "info": "ℹ️", "default": "💡"}
    def callout(m: re.Match) -> str:
        tm = re.search(r'type="(\w+)"', m.group(1) or "")
        mark = marks.get(tm.group(1) if tm else "default", "💡")
        inner = m.group(2).strip()
        return "\n".join(f"> {mark} {ln}" if i == 0 else f"> {ln}"
                         for i, ln in enumerate(inner.splitlines()))
    mdx = re.sub(r"<Callout([^>]*)>(.*?)</Callout>", callout, mdx, flags=re.S)
    # <Tabs items={['a','b']}> <Tabs.Tab>..</Tabs.Tab> </Tabs> -> 分组小节
    def tabs(m: re.Match) -> str:
        items = re.findall(r"['\"]([^'\"]+)['\"]", m.group(1) or "")
        panes = re.findall(r"<Tabs\.Tab>(.*?)</Tabs\.Tab>", m.group(2), re.S)
        out = []
        for i, pane in enumerate(panes):
            label = items[i] if i < len(items) else f"选项 {i + 1}"
            out.append(f"**{label}**\n\n{pane.strip()}")
        return "\n\n".join(out)
    mdx = re.sub(
        r"<Tabs\s+items=\{\[(.*?)\]\}[^>]*>(.*?)</Tabs>", tabs, mdx, flags=re.S
    )
    # 索引页表格里的图标组件
    mdx = re.sub(r"<IntegrationToolIcon[^>]*/>\s*", "", mdx)
    # 剩余未知组件提示（保留原文，仅告警）
    leftover = sorted(set(re.findall(r"<([A-Z][A-Za-z.]*)", mdx)))
    if leftover:
        print(f"  [note] 保留未转换组件: {leftover}")
    return mdx


def transform(mdx: str, locale: str, page_path: str, all_paths: set) -> str:
    md_file = md_file_for(page_path, all_paths)
    mdx = localize_images(mdx, locale, page_path, md_file)
    mdx = rewrite_md_links(mdx, md_file, all_paths)
    mdx = clean_jsx(mdx)
    mdx = rebrand(mdx)
    return mdx.strip() + "\n"


# ---------------------------------------------------------------- Nextra 站点

DOCS_SITE = ROOT / "docs-site"


def front_title(mdx: str) -> str | None:
    m = re.match(r"^---\n(.*?)\n---", mdx, re.S)
    if m:
        t = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', m.group(1), re.M)
        if t:
            return t.group(1)
    return None


def appearance_order(mdx: str, candidates: set) -> list:
    """按 mdx 中链接出现顺序排列 candidates，未出现的按字母序放最后。"""
    order = []
    for link in re.findall(
        rf"(?<!images)/(?:docs/)?(?:zh|en)/{SECTION}/([a-zA-Z0-9/_-]+)", mdx
    ):
        link = link.strip("/").split("#")[0]
        if link in candidates and link not in order:
            order.append(link)
    return order + sorted(candidates - set(order))


def nav_orders(pages: dict) -> dict:
    """计算侧边栏顺序：{目录相对路径: [有序 slug 列表]}，顺序取自索引页表格。"""
    modules = {p.split("/")[0] for p in pages if p}
    orders = {"": appearance_order(pages[""], modules)}
    for mod in modules:
        children = {p[len(mod) + 1:] for p in pages if p.startswith(mod + "/")}
        if children:
            orders[mod] = appearance_order(pages.get(mod, ""), children)
    return orders


def js_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def md_title(md_path: Path) -> str:
    """取一个 markdown 文件的标题：frontmatter title，退化为 H1，再退化为文件名。"""
    text = md_path.read_text(encoding="utf-8")
    t = front_title(text)
    if not t:
        m = re.search(r"^# (.+)$", text, re.M)
        t = m.group(1).strip() if m else md_path.stem
    return t


def export_page(src: Path, dst: Path) -> None:
    """把 markdown/ 下的文件转成 Nextra content 页面：图片与内链改为站内绝对路径。"""
    text = src.read_text(encoding="utf-8")
    rel_dir = src.parent.relative_to(OUT)  # 如 zh/claude-code

    def fix_link(m: re.Match) -> str:
        prefix, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", target) or target.startswith(("#", "/")):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = os.path.normpath(str(rel_dir / path)).replace(os.sep, "/")
        if resolved.split("/")[0] == "assets":  # 图片 -> public 静态路径
            route = "/" + resolved
        else:  # 页面 -> 去掉 .md 的路由（trailingSlash）
            route = "/" + re.sub(r"(?:^|/)index\.md$|\.md$", "", resolved)
            route = route.rstrip("/") + "/"
        return f"{prefix}{route}{'#' + anchor if anchor else ''}"

    text = re.sub(r'(\]\(|href=")([^)"\s]+)', fix_link, text)
    save(dst, text)


def export_nextra() -> None:
    """把 markdown/ 内容导出为 docs-site/ 的 Nextra 站点源（content + public）。"""
    import shutil

    orders = json.loads((OUT / "nav.json").read_text(encoding="utf-8"))
    content = DOCS_SITE / "content"
    shutil.rmtree(content, ignore_errors=True)
    shutil.rmtree(DOCS_SITE / "public" / "assets", ignore_errors=True)
    shutil.copytree(OUT / "assets", DOCS_SITE / "public" / "assets")

    labels = {"zh": "中文", "en": "English"}
    top = ["export default {", "  index: { display: 'hidden' },"]
    for locale in LOCALES:
        top.append(f"  {locale}: {{ type: 'page', title: {js_str(labels.get(locale, locale))} }},")
    save(content / "_meta.js", "\n".join(top) + "\n}\n")
    save(
        content / "index.md",
        f"---\ntitle: {SITE_NAME} Docs\n---\n\n# {SITE_NAME} 工具集成文档\n\n"
        f"- [中文文档](/zh/)\n- [English Docs](/en/)\n",
    )

    for locale in LOCALES:
        for src in (OUT / locale).rglob("*.md"):
            export_page(src, content / src.relative_to(OUT))
        # 每个目录的 _meta.js 控制侧边栏顺序与标题
        for dirname, slugs in orders[locale].items():
            base = OUT / locale / dirname
            lines = ["export default {"]
            entries = ["index"] + slugs if (base / "index.md").exists() else slugs
            for slug in entries:
                if (base / slug).is_dir():
                    title = md_title(base / slug / "index.md")
                elif (base / f"{slug}.md").exists():
                    title = md_title(base / f"{slug}.md")
                else:
                    continue
                lines.append(f"  {js_str(slug)}: {js_str(title)},")
            save(content / locale / dirname / "_meta.js", "\n".join(lines) + "\n}\n")

    save(
        DOCS_SITE / "site-config.mjs",
        f"export default {{\n  siteName: {js_str(SITE_NAME)},\n"
        f"  siteUrl: {js_str(SITE_URL)},\n"
        f"  description: {js_str(SITE_NAME + ' 工具集成文档')}\n}}\n",
    )
    pages_n = len(list(content.rglob("*.md")))
    print(f"已导出 Nextra 站点源: docs-site/content ({pages_n} 页)")


def run_npm(*npm_args: str) -> None:
    import shutil

    if not shutil.which("npm"):
        print("未找到 npm，请先安装 Node.js 20+")
        sys.exit(1)
    if not (DOCS_SITE / "node_modules").exists():
        print("== 首次运行，安装依赖 (npm install) ...")
        subprocess.run(["npm", "install", "--no-audit", "--no-fund"],
                       cwd=DOCS_SITE, check=True)
    proc = subprocess.run(["npm", *npm_args], cwd=DOCS_SITE)
    if proc.returncode:
        sys.exit(proc.returncode)


# ---------------------------------------------------------------- 主流程

def build() -> None:
    print(f"输出目录: {OUT}")
    total_pages = 0
    all_orders = {}
    for locale in LOCALES:
        print(f"== 抓取 {locale} ...")
        pages = crawl(locale)
        all_paths = set(pages)
        for page_path, mdx in sorted(pages.items()):
            md_file = md_file_for(page_path, all_paths)
            save(OUT / locale / md_file, transform(mdx, locale, page_path, all_paths))
        all_orders[locale] = nav_orders(pages)
        total_pages += len(pages)
    save(OUT / "nav.json", json.dumps(all_orders, ensure_ascii=False, indent=1))

    zh_n = len(list((OUT / "zh").rglob("*.md")))
    en_n = len(list((OUT / "en").rglob("*.md")))
    img_n = sum(1 for p in (OUT / "assets").rglob("*") if p.is_file()) \
        if (OUT / "assets").exists() else 0
    save(
        OUT / "README.md",
        f"# {SITE_NAME} 工具集成文档\n\n"
        f"- [中文文档](zh/index.md)（{zh_n} 页）\n"
        f"- [English docs](en/index.md)（{en_n} 页）\n"
        f"- 图片资源: `assets/<模块名>/`（{img_n} 张）\n\n"
        f"由 `generate_integrations.py` 生成，内容为原站每页"
        f"「Copy page as Markdown」的 Markdown 源码。\n",
    )
    print(f"\n完成: {total_pages} 个页面 (zh {zh_n} / en {en_n}), {img_n} 张图片")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--site-name", help="站点名称，替换内容中的 HaoAI 等品牌文字")
    ap.add_argument("--site-url", help="站点 URL，替换内容中指向 https://hao.ai 的链接")
    ap.add_argument("--fetch", action="store_true",
                    help="重新从原站抓取一次，刷新本地 markdown/（默认不抓取，用本地内容）")
    ap.add_argument("--build", action="store_true",
                    help="生成后构建静态站点到 docs-site/out/")
    ap.add_argument("--dev", "--serve", dest="dev", action="store_true",
                    help="生成后启动本地预览 (Next.js dev)")
    args = ap.parse_args()
    load_config(args)

    # 只抓一次：默认用本地 markdown/；本地没有内容或显式 --fetch 时才抓取
    has_local = (OUT / "nav.json").exists()
    if args.fetch or not has_local:
        if not has_local and not args.fetch:
            print("未发现本地 markdown/ 内容，首次自动抓取一次 ...")
        build()
    else:
        print("使用本地 markdown/ 内容（跳过抓取）。如需从原站更新，请加 --fetch")

    export_nextra()
    if args.build:
        run_npm("run", "build")
        print(f"静态站点已输出到 {DOCS_SITE / 'out'}")
    if args.dev:
        run_npm("run", "dev")
