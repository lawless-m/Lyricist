#!/usr/bin/env python3
"""Serve the track list from lighttpd, built fresh from the database.

Symlinked into /usr/lib/cgi-bin/catalogue and aliased to /catalogue by
/etc/lighttpd/conf-enabled/15-catalogue.conf, following the pattern the glossy
endpoints on this box already use.

Built per request rather than cached, so a `tools/db.py sync` shows up on a
refresh with nothing to regenerate. The connection is read-only: the web server
can read the repo but must never be able to write to it.
"""

import sys
import traceback
from pathlib import Path

# resolve() walks the symlink back to the repo, which is where db and page live.
sys.path.insert(0, str(Path(__file__).resolve().parent))


def main():
    import db
    import page
    con = db.read_only()
    try:
        body = page.wrap(db.markup(con)).encode("utf-8")
    finally:
        con.close()
    sys.stdout.write("Content-Type: text/html; charset=utf-8\r\n")
    sys.stdout.write("Cache-Control: no-store\r\n")
    sys.stdout.write(f"Content-Length: {len(body)}\r\n\r\n")
    sys.stdout.flush()
    sys.stdout.buffer.write(body)


try:
    main()
except Exception:
    # A CGI that dies silently gives the browser a blank 500 and tells you
    # nothing, so hand the traceback back as the page.
    detail = traceback.format_exc()
    sys.stdout.write("Status: 500 Internal Server Error\r\n")
    sys.stdout.write("Content-Type: text/plain; charset=utf-8\r\n\r\n")
    sys.stdout.write(detail)
