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


def get_or(form: dict, key: str, fallback: int) -> int:
    res = form.get(key, fallback)
    if not res:
        return fallback
    return int(res)


def query(form: dict):
    hp_min, hp_max = get_or(form, "hp_min", 0), get_or(form, "hp_max", 1000)
    hp_rng = range(hp_min, hp_max)
    atk_min, atk_max = (
        get_or(form, "atk_min", 0),
        get_or(form, "atk_max", 1000),
    )
    atk_rng = range(atk_min, atk_max)
    def_min, def_max = (
        get_or(form, "def_min", 0),
        get_or(form, "def_max", 1000),
    )
    def_rng = range(def_min, def_max)

    def f_tp(monster):
        return True

    tp_1 = form.get("tp_1")
    if tp_1 is not None:

        def f_tp(monster):
            return monster["Type 1"] == res

    res = [
        monster
        for monster in app.data
        if f_tp(monster)
        and monster["Health"] in hp_rng
        and monster["Attack"] in atk_rng
        and monster["Defense"] in def_rng
    ]
    return res
