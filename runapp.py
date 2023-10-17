#!/usr/bin/env python
import os

from paste.deploy import loadapp
from waitress import serve

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = "0.0.0.0"

    database = os.getenv("DATABASE_URL")

    if not database:
        raise ValueError("DATABASE_URL is not correctly defined: %s" %
                         database)

    app = loadapp('config:bot.py', relative_to='.')

    serve(app, host=host, port=port)
