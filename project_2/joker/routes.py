#!/usr/bin/env python3

from flask import (
    Blueprint,
    abort,
    current_app,
    render_template,
    request,
)

from joker.logic import query

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    """Render the template with form"""
    # TODO: Implement this function
    return render_template("index.html", jokes=[])


@main.post("/")
def post_index():
    """Render the template with jokes"""
    # TODO: Implement this function
    form = request.form
    lang = form["lang"]
    cat = form["cat"]
    num = form["num"]
    if (lang == "es" and cat == "chuck") or (cat == "twister" and lang != "de"):
        abort(404)
    print(form)
    res = query(form["lang"], form["cat"], form["num"])
    return render_template("index.html", jokes=res)


@main.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found error"""
    # TODO: Implement this function
    abort(404)
