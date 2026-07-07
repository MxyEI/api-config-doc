# api-config-doc

## 工具集成文档站点

把本地 `markdown/` 下的教程内容生成为一个 Nextra 文档站点，中英双语、按模块分目录，
图片全部存放在本地。`markdown/` 就是内容源，日常改内容后重建站点即可。

### 一键生成

```bash
python3 generate_integrations.py            # 用本地 markdown/ 生成 docs-site/
python3 generate_integrations.py --dev      # 生成后启动本地预览（Next.js dev）
python3 generate_integrations.py --build    # 生成后构建静态站点到 docs-site/out/
```

生成脚本仅依赖 Python 3 标准库；预览 / 构建站点需要 Node.js 20+（首次会自动 `npm install`）。

### 生成自己的文档站点

站点用 [Nextra 4](https://nextra.site)（`nextra-theme-docs`）构建，源码在 `docs-site/`，
主色与内容宽度在 `docs-site/app/globals.css` 里配置。侧边栏顺序取自索引页表格。

- 本地预览：`python3 generate_integrations.py --dev`（默认 http://localhost:3000）
- 构建产物：`docs-site/out/` 目录，纯静态文件（含 Pagefind 全文搜索），可部署到任意静态托管 / Nginx / GitHub Pages
- 改完 `markdown/` 内容后，直接 `python3 generate_integrations.py` 重建站点

### 站点品牌配置

生成时会把内容中的站点品牌替换为你配置的站点名称和 URL。
优先级：命令行参数 > `site.config.json` > 内置默认值。

```jsonc
// site.config.json
{
  "site_name": "Look2Eye",
  "site_url": "https://api.look2eye.com"
}
```

```bash
# 也可以用命令行参数临时覆盖
python3 generate_integrations.py --site-name "MyAPI" --site-url "https://api.example.com"
```

品牌替换覆盖正文、代码示例、frontmatter 和图片文件名中的名称 / 域名 / URL / 环境变量名 / 锚点等形式。

### 输出结构（按模块区分）

```
markdown/
├── README.md                      # 目录索引
├── zh/                            # 中文（31 页）
│   ├── index.md                   # 集成索引页（工具总表）
│   ├── cline.md                   # 单页模块
│   ├── claude-code/               # 带子页的模块
│   │   ├── index.md               # 概览
│   │   ├── installation.md
│   │   ├── model-provider.md
│   │   ├── contextline.md
│   │   └── skills.md
│   └── ...
├── en/                            # 英文，结构与中文一致（31 页）
└── assets/<模块名>/*.webp          # 图片按模块归类（207 张）
```

### 生成脚本做了什么

1. 遍历 `markdown/` 下的中英文页面，按模块及嵌套子页组织导航（新增页面无需改代码）；
2. 把内容导出为 Nextra 站点源（`docs-site/content` + `docs-site/public/assets`）：
   图片链接改为站内绝对路径，文档互链改为站内路由；
3. 按 `site.config.json` 应用品牌替换后，生成侧边栏顺序与标题（`_meta.js`）。

### 已知限制

- 代码示例中的 `<YOUR_API_KEY>` 等占位符按原样保留；
- 对外发布前请确认内容与截图已获授权或替换为自己的素材。
```
