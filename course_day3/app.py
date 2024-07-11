#!/usr/bin/env python3

from data_exploration import read_csv
from flask import Flask, abort, render_template, request


def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokemon.csv")
    types, generations = set(), set()
    for item in app.data:
        types.add(item["Type 1"])
        if item["Type 2"]:
            types.add(item["Type 2"])
        generations.add(item["Generation"])
    app.types = sorted(types)
    app.generations = sorted(generations)

    return app


app = create_app()


@app.get("/")
def get_index():
    return render_template(
        "query_form.html",
        types=app.types,
        generations=app.generations,
    )


@app.post("/")
def post_index():
    print(request.form)
    if request.form:
        return render_template("index.html", data=query(dict(request.form)))
    else:
        return "What?!"


@app.route("/<int:pokemon_id>")
def pok_by_id(pokemon_id: int):
    try:
        data = next(m for m in app.data if int(m["ID"]) == pokemon_id)
    except IndexError:
        abort(404)
    return render_template("details.html", data=data)


def query(form: dict):
    result = []
    hp_min = int(form.get("hp_min", -1))
    hp_max = int(form.get("hp_max", 1000))
    hp_range = range(hp_min, hp_max)
    for monster in app.data:
        if monster["Type 1"] != form["primary_type"]:
            continue
        if monster["Health"] not in hp_range:
            continue
        result.append(monster)

    return result
