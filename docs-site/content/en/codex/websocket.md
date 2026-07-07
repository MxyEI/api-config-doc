---
title: "Enable WebSocket"
description: "Enable the recommended WebSocket connection for Codex local clients while keeping the Look2Eye API key in CC Switch"
---


# Enable WebSocket

Complete [Configure Model Provider](/en/codex/model-provider/) first, then run the one-line command to enable the Codex Responses protocol format and WebSocket connection. The script only updates connection capability. It does not read, save, or overwrite your API key.

## Enable WebSocket in One Command (Recommended)

```bash
#!/usr/bin/env sh
set -eu

look2eye_setup_result() {
  rc=$?
  if [ "$rc" -eq 0 ]; then
    printf '\n'
    echo "============================================================"
    echo "[LOOK2EYE SETUP SUCCESS] 看两眼 Codex CLI 配置已完成。"
    echo "请重新打开 Codex 或对应客户端，让新配置生效。"
    echo "============================================================"
  else
    printf '\n' >&2
    echo "============================================================" >&2
    echo "[LOOK2EYE SETUP FAILED] 看两眼 Codex CLI 配置未完成或未完全生效。退出码：$rc" >&2
    echo "请查看上方失败原因；如提示 Codex 未关闭，请手动关闭后重试。" >&2
    echo "============================================================" >&2
  fi
  trap - EXIT
  exit "$rc"
}
trap look2eye_setup_result EXIT

## 替换这里的 key
BASE_URL='https://api.look2eye.com'
API_KEY='xxxxxx'
ENABLE_WEBSOCKET='true'
CONFIG_TOML_TEMPLATE='model_provider = "Look2eye"
model = "gpt-5.5"
review_model = "gpt-5.5"
model_reasoning_effort = "xhigh"
model_context_window = 1000000
model_auto_compact_token_limit = 900000
disable_response_storage = true
network_access = "enabled"
windows_wsl_setup_acknowledged = true

[agents]
max_threads = 20
max_depth = 1

[model_providers.Look2eye]
name = "Look2eye"
base_url = "{{LOOK2EYE_BASE_URL}}"
wire_api = "responses"
supports_websockets = {{LOOK2EYE_ENABLE_WEBSOCKET}}

[features]
responses_websockets_v2 = {{LOOK2EYE_ENABLE_WEBSOCKET}}
goals = true

[windows]
sandbox = "elevated"
'
CODEX_DIR="$HOME/.codex"
CONFIG_PATH="$CODEX_DIR/config.toml"
AUTH_PATH="$CODEX_DIR/auth.json"
BACKUP_DIR="$CODEX_DIR/backups"

mkdir -p "$CODEX_DIR" "$BACKUP_DIR"

stop_codex_processes() {
  if [ "${LOOK2EYE_SKIP_CODEX_PROCESS_CLOSE:-}" = "1" ]; then
    echo "已跳过结束 Codex 进程。"
    return 0
  fi

  if ! command -v pkill >/dev/null 2>&1; then
    echo "配置已写入，但未找到 pkill，无法自动结束 Codex 进程。请手动关闭 Codex 后重新打开。" >&2
    return 1
  fi

  stopped=0
  failed=0
  for process_name in codex Codex; do
    count=0
    if command -v pgrep >/dev/null 2>&1; then
      count=$(pgrep -x "$process_name" 2>/dev/null | wc -l | tr -d ' ')
    fi
    if pkill -x "$process_name" >/dev/null 2>&1; then
      if [ "${count:-0}" -gt 0 ]; then
        stopped=$((stopped + count))
      else
        stopped=$((stopped + 1))
      fi
    elif [ "${count:-0}" -gt 0 ]; then
      failed=1
    fi
  done

  if [ "$stopped" -gt 0 ]; then
    echo "已结束 Codex 进程：$stopped 个。"
  else
    echo "未发现正在运行的 Codex 进程；重新打开 Codex 即可使用新配置。"
  fi
  if [ "$failed" -ne 0 ]; then
    echo "配置已写入，但部分 Codex 进程无法自动关闭。请手动关闭 Codex 后重新打开。" >&2
    return 1
  fi
  return 0
}

new_backup_stamp() {
  base=$(date +"%Y%m%d-%H%M%S")
  stamp="$base"
  counter=2
  while [ -e "$BACKUP_DIR/$(basename "$CONFIG_PATH").bak-$stamp" ] || [ -e "$BACKUP_DIR/$(basename "$AUTH_PATH").bak-$stamp" ]; do
    stamp="$base-$(printf "%02d" "$counter")"
    counter=$((counter + 1))
  done
  printf '%s\n' "$stamp"
}

PYTHON_BIN=
if command -v python3 >/dev/null 2>&1 && python3 -c 'import sys' >/dev/null 2>&1; then
  PYTHON_BIN=python3
elif command -v python >/dev/null 2>&1 && python -c 'import sys' >/dev/null 2>&1; then
  PYTHON_BIN=python
else
  echo "失败：需要可用的 python3 或 python 才能安全合并或恢复现有 Codex 配置。" >&2
  exit 1
fi

LOOK2EYE_ACTION=${1:-apply}

case "$LOOK2EYE_ACTION" in
  ""|1|apply|--apply)
    printf "\n看两眼 Codex CLI 一键配置：默认覆盖当前配置。\n"
    echo "如需恢复备份，请在终端运行本脚本并追加 restore 参数。"
    ;;
  2|restore|--restore|/restore)
    "$PYTHON_BIN" - "$CONFIG_PATH" "$AUTH_PATH" "$BACKUP_DIR" <<'PY'
import shutil
import sys
from datetime import datetime
from pathlib import Path

config_path = Path(sys.argv[1])
auth_path = Path(sys.argv[2])
backup_dir = Path(sys.argv[3])

def collect(path, kind, sets):
    prefix = path.name + ".bak-"
    for directory in (backup_dir, path.parent):
        if not directory.exists():
            continue
        for candidate in directory.glob(prefix + "*"):
            if not candidate.is_file():
                continue
            stamp = candidate.name[len(prefix):]
            entry = sets.setdefault(stamp, {"timestamp": stamp, "config": None, "auth": None, "mtime": 0.0})
            candidate_mtime = candidate.stat().st_mtime
            if entry[kind] is None or candidate_mtime > entry[kind].stat().st_mtime:
                entry[kind] = candidate
            entry["mtime"] = max(entry["mtime"], candidate_mtime)

sets = {}
collect(config_path, "config", sets)
collect(auth_path, "auth", sets)
items = sorted(sets.values(), key=lambda item: item["mtime"], reverse=True)
if not items:
    raise SystemExit("失败：未找到之前的 Codex config/auth 备份。")

print("")
print("可用备份：")
for index, item in enumerate(items, 1):
    labels = {"config": "配置", "auth": "认证"}
    parts = "+".join(labels[kind] for kind in ("config", "auth") if item[kind] is not None)
    file_time = datetime.fromtimestamp(item["mtime"]).strftime("%Y-%m-%d %H:%M:%S")
    print(f"{index}) {item['timestamp']} [{parts}] 文件时间 {file_time}")

choice = input("请选择备份序号：").strip()
try:
    selected = items[int(choice) - 1]
except (ValueError, IndexError):
    raise SystemExit("失败：备份序号无效。")

if selected["config"] is not None:
    shutil.copy2(selected["config"], config_path)
    print(f"已恢复：{config_path}")
if selected["auth"] is not None:
    shutil.copy2(selected["auth"], auth_path)
    print(f"已恢复：{auth_path}")
print("已完成，之前的 Codex 配置已恢复。")
PY
    stop_codex_processes
    exit 0
    ;;
  *)
    echo "失败：参数无效：$LOOK2EYE_ACTION。直接运行会配置 看两眼；恢复备份请使用 restore 参数。" >&2
    exit 1
    ;;
esac

timestamp=$(new_backup_stamp)
if [ -f "$CONFIG_PATH" ]; then
  config_backup="$BACKUP_DIR/$(basename "$CONFIG_PATH").bak-$timestamp"
  cp "$CONFIG_PATH" "$config_backup"
  echo "已备份：$config_backup"
fi
if [ -f "$AUTH_PATH" ]; then
  auth_backup="$BACKUP_DIR/$(basename "$AUTH_PATH").bak-$timestamp"
  cp "$AUTH_PATH" "$auth_backup"
  echo "已备份：$auth_backup"
fi

"$PYTHON_BIN" - "$CONFIG_PATH" "$AUTH_PATH" "$BASE_URL" "$API_KEY" "$ENABLE_WEBSOCKET" "$CONFIG_TOML_TEMPLATE" <<'PY'
import json
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
auth_path = Path(sys.argv[2])
base_url = sys.argv[3].rstrip("/")
api_key = sys.argv[4].strip()
enable_ws = sys.argv[5].lower() == "true"
template = sys.argv[6]

if not api_key:
    raise RuntimeError("缺少 API Key。")
if not base_url:
    raise RuntimeError("缺少 Base URL。")

if auth_path.exists() and auth_path.read_text(encoding="utf-8").strip():
    try:
        json.loads(auth_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError("auth.json 不是合法 JSON，请手动合并后重试。") from exc

rendered_config = template.replace("{{LOOK2EYE_BASE_URL}}", base_url)
rendered_config = rendered_config.replace("{{LOOK2EYE_ENABLE_WEBSOCKET}}", "true" if enable_ws else "false")
rendered_config = rendered_config.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n") + "\n"
auth_text = json.dumps({"OPENAI_API_KEY": api_key}, ensure_ascii=False, separators=(",", ":")) + "\n"

config_path.write_text(rendered_config, encoding="utf-8")
auth_path.write_text(auth_text, encoding="utf-8")

if config_path.read_text(encoding="utf-8") != rendered_config:
    raise RuntimeError("config.toml 写入后回读不一致，请检查磁盘权限或安全软件拦截。")
actual_auth = json.loads(auth_path.read_text(encoding="utf-8"))
if actual_auth.get("OPENAI_API_KEY") != api_key:
    raise RuntimeError("auth.json 写入后 API Key 校验失败。")
PY

echo "回读校验：已确认配置和认证文件写入成功。"
echo "已完成，看两眼 Codex CLI 配置已更新。正在自动关闭 Codex..."
stop_codex_processes

ensure_codex_client() {
  if command -v codex >/dev/null 2>&1; then
    codex --version 2>/dev/null || true
    return 0
  fi

  echo "[LOOK2EYE NOTICE] 未检测到 Codex CLI，准备通过 npm 全局安装。"
  if ! command -v npm >/dev/null 2>&1; then
    echo "未检测到 npm，无法自动安装 Codex CLI。请先安装 Node.js LTS：https://nodejs.org/" >&2
    echo "安装 Node.js 后可手动执行：npm install -g @openai/codex" >&2
    return 0
  fi

  if npm install -g @openai/codex; then
    if command -v codex >/dev/null 2>&1; then
      codex --version 2>/dev/null || true
    else
      echo "Codex CLI 已安装，但当前终端仍未检测到 codex；请重新打开终端后再运行客户端。" >&2
    fi
  else
    echo "Codex CLI 自动安装失败，请手动执行：npm install -g @openai/codex" >&2
  fi
}

ensure_codex_client
```

The script backs up `~/.codex/config.toml`, finds the Look2Eye provider written by CC Switch when possible, and adds these fields to the existing provider block. The example below uses `look2eye` as the provider name; if your local provider uses another name, replace `look2eye` with that name:

```toml
[model_providers.look2eye]
wire_api = "responses"
supports_websockets = true
```

> ℹ️ `wire_api = "responses"` tells Codex to use the Responses protocol format; `supports_websockets = true` tells Codex this provider supports a WebSocket connection. Together, they let Codex connect to Look2Eye through the recommended path.
> 
> The API key stays in the CC Switch Codex provider settings. This command only enables the Codex protocol format and WebSocket connection.
> 
> If your config uses an inline table under `[model_providers]`, the script updates the existing provider entry instead of forcing another TOML layout.
