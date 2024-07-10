#!/usr/bin/env python3

from data_exploration import read_csv
from flask import Flask, abort, render_template


def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokemon.csv")
    return app


app = create_app()


@app.route("/")
def index():
    return render_template("index.html", data=app.data)
    # return render_template("index.html", data=[])


@app.route("/<int:pokemon_id>")
def pok_by_id(pokemon_id: int):
    try:
        data = [m for m in app.data if int(m["#"]) == pokemon_id][0]
    except IndexError:
        abort(404)
    return render_template("details.html", data=data, name=data["Name"])
