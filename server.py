import json
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    # print all received headers
    out = ""
    for header in sorted(dict(request.headers)):
        out += f"<b>{header}</b>: {request.headers[header]}<br>"
    return out


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
