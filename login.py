import os
import sys
import http.cookiejar
import io
from pathlib import Path

def run():
    # クッキーファイルのパス（リポジトリルート）
    cookie_text_path = Path(__file__).parent / "atcoder_cookies.txt"
    
    if not cookie_text_path.exists():
        print(f"[-] Error: '{cookie_text_path.name}' not found in the repository root.", file=sys.stderr)
        print("    Please create it and paste your AtCoder cookies in Netscape format.", file=sys.stderr)
        return

    with open(cookie_text_path, "r", encoding="utf-8") as f:
        netscape_data = f.read()

    if not netscape_data.strip():
        print(f"[-] Error: '{cookie_text_path.name}' is empty.", file=sys.stderr)
        print("    Please paste your AtCoder cookies in Netscape format before running this script.", file=sys.stderr)
        return

    # online-judge-tools のクッキー保存先
    local_app_data = os.environ.get("LOCALAPPDATA")
    if not local_app_data:
        print("[-] Error: LOCALAPPDATA environment variable is not set.", file=sys.stderr)
        return
        
    path = Path(local_app_data) / "online-judge-tools" / "online-judge-tools" / "cookie.jar"
    
    # Netscape -> LWP 変換
    mcj = http.cookiejar.MozillaCookieJar()
    try:
        mcj._really_load(io.StringIO(netscape_data), "mem", False, False)
    except Exception as e:
        print(f"[-] Error parsing cookie data: {e}", file=sys.stderr)
        print("    Ensure the file is strictly in Netscape cookie format.", file=sys.stderr)
        return

    lcj = http.cookiejar.LWPCookieJar()
    for c in mcj:
        lcj.set_cookie(c)
    
    # 注入
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        lcj.save(str(path), ignore_discard=True, ignore_expires=True)
        print(f"[+] Successfully injected AtCoder cookies into:")
        print(f"    {path}")
    except Exception as e:
        print(f"[-] Error saving cookies: {e}", file=sys.stderr)

if __name__ == "__main__":
    run()