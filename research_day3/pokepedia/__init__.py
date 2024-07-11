#!/usr/bin/env python3

from pokepedia.data_exploration import read_csv
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokepedia/data/pokemon.csv")
    types, generations = set(), set()
    for item in app.data:
        types.add(item["Type 1"])
        if item["Type 2"]:
            types.add(item["Type 2"])
        generations.add(item["Generation"])
    app.types = sorted(types)
    app.generations = sorted(generations)
    from pokepedia.routes import main

    app.register_blueprint(main)

    return app
