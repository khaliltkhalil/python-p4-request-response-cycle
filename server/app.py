#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, redirect, abort

app = Flask(__name__)


@app.before_request
def app_path():
    # print(g.path)
    g.pat = os.path.abspath(os.getcwd())


@app.route("/")
def index():
    host = request.headers.get("Host")
    appname = current_app.name
    return f"""<h1>The host for this page is {host}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.pat}</h3>"""


@app.route("/user")
def user():
    abort(404)
    return "hi"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
