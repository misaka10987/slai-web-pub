#!/usr/bin/env python3

from flask import Blueprint, abort, render_template, request, current_app

from pokepedia.logic import query

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    return render_template(
        "query_form.html",
        types=current_app.types,
        generations=current_app.generations,
    )


@main.post("/")
def post_index():
    print(request.form)
    if request.form:
        return render_template("index.html", data=query(dict(request.form)))
    else:
        return "What?!"


@main.route("/<int:pokemon_id>")
def pok_by_id(pokemon_id: int):
    try:
        data = next(m for m in current_app.data if int(m["ID"]) == pokemon_id)
    except Exception:
        abort(404)
    return render_template("details.html", data=data)
