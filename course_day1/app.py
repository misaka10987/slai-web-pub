#!/usr/bin/env python3
from flask import Flask, abort
from data_exploration import read_csv


def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokemon.csv")
    return app


app = create_app()


@app.route("/")
def index():
    return "Hello, SLAI web developers!"


@app.route("/<int:pok_id>")
def pok_by_id(pok_id):
    for monster in app.data:
        if int(monster["#"]) == pok_id:
            return f"<strong>{monster['Name']}</strong>"
    abort(404)
