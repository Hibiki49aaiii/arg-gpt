#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.server
import socketserver
import threading
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITES = ROOT / "sites"

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Start the District Eight Act 0-1 Blind Playtest server."
    )
    p.add_argument("--host", default="127.0.0.1", help="Bind host (default: 127.0.0.1)")
    p.add_argument("--port", type=int, default=8000, help="Bind port (default: 8000)")
    p.add_argument(
        "--no-browser",
        action="store_true",
        help="Do not open the facilitator control page automatically.",
    )
    return p.parse_args()

def main() -> None:
    args = parse_args()
    if not SITES.exists():
        raise SystemExit(f"sites directory not found: {SITES}")

    handler = lambda *a, **kw: http.server.SimpleHTTPRequestHandler(
        *a, directory=str(SITES), **kw
    )

    control_url = f"http://{args.host}:{args.port}/meta/playtest.html"
    entry_url = f"http://{args.host}:{args.port}/old-bousai/"

    class Server(socketserver.ThreadingTCPServer):
        allow_reuse_address = True

    with Server((args.host, args.port), handler) as httpd:
        print("District Eight Blind Playtest")
        print("=" * 31)
        print(f"Facilitator control: {control_url}")
        print(f"Tester entry:        {entry_url}")
        print()
        print("Before each session:")
        print("1. Open facilitator control")
        print("2. Enter anonymous Session ID")
        print("3. Reset session state")
        print("4. Give only the Tester entry URL to the tester")
        print("5. After session, export JSON from facilitator control")
        print()
        print("Press Ctrl+C to stop.")

        if not args.no_browser:
            threading.Timer(0.5, lambda: webbrowser.open(control_url)).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    main()
