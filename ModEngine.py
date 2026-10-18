#!/usr/bin/env python3
"""
XENO-MOD Launcher
Serves the Godot-style Gen1Recomp Mod Engine and opens it in the default browser.
Desktop-shortcut friendly.
"""
import http.server
import socketserver
import webbrowser
import threading
import os
from pathlib import Path

PORT = 8765
EDITOR_DIR = Path(__file__).parent / "editor"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(EDITOR_DIR), **kwargs)

    def log_message(self, format, *args):
        pass

def open_browser():
    webbrowser.open(f"http://127.0.0.1:{PORT}")

def main():
    os.chdir(EDITOR_DIR.parent)
    print("XENO-MOD // Gen1Recomp Engine")
    print("Based on the Pokemon Gen 1 Recompilation Project by BOIS CLUB GAMES, LLC")
    print("https://github.com/bryanthaboi/gen1recomp")
    print(f"\nServing editor at http://127.0.0.1:{PORT}")
    print("Close this window to stop the engine.\n")

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        threading.Timer(0.8, open_browser).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[XENO] Lattice closed.")

if __name__ == "__main__":
    main()
