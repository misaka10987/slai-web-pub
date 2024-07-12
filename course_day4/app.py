#!/usr/bin/env python3

import csv
import pathlib
from flask import Flask, make_response, render_template, request, redirect, url_for

from werkzeug.utils import secure_filename


def create_app():
    app = Flask(__name__)

    return app


app = create_app()


@app.route("/")
def index():
    try:
        with open(
            pathlib.Path(__file__).parent.absolute()
            / pathlib.Path("uploads")
            / pathlib.Path(request.cookies.get("display_file")),
            "r",
            encoding="utf8",
        ) as f:
            data = csv.DictReader(f)
            return render_template("index.html", data=data)
    except FileNotFoundError:
        # return "File not Found"
        return render_template("index.html")
    except TypeError:
        return render_template("index.html")


@app.post("/upload")
def upload():
    f = request.files["file"]
    f.save(
        pathlib.Path(__file__).parent.absolute()
        / pathlib.Path("uploads")
        / pathlib.Path(secure_filename(f.filename))
    )

    resp = make_response(redirect(url_for("index")))
    resp.set_cookie("display_file", secure_filename(f.filename))
    return resp
