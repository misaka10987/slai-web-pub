#!/usr/bin/env python3
"""
Flask app routes

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask import (
    Blueprint,
    abort,
    render_template,
    request,
    redirect,
    url_for,
)

from plucky.logic import lucky_number

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    return render_template("index.html")


@main.post("/")
def post_index():
    if not request.form:
        return redirect(url_for("main.get_index"), 303)
    the_lucky_number = lucky_number(1, 6)
    return render_template(
        "index.html", data=the_lucky_number, guess=int(request.form.get("guess"))
    )


@main.get("/about")
def about():
    return render_template("about.html")


@main.get("/<path:path>")
def catch_all(path):
    abort(404)


@main.errorhandler(404)
def not_found(error):
    return render_template("not_found.html"), 404
