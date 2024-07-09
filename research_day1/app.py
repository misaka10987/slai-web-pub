#!/usr/bin/env python3

from string import Template

from data_exploration import read_csv
from flask import Flask, abort, make_response


def create_app():
    app = Flask(__name__)
    app.data = read_csv("pokemon.csv")
    return app


app = create_app()


@app.route("/")
def index():
    """Use template string to have a welcome message"""


@app.route("/<int:pok_id>")
def pok_by_id(pok_id: int):
    """Return properties of the pokemon with the specified id
    abort with error 404 if there is an error
    """


@app.route("/api/<int:pok_id>")
def pok_json_by_id(pok_id: int):
    """Return properties of the pokemon with the specified id as JSON
    abort with error 404 if there is an error
    """


@app.route("/attack/<int:min_val>/<int:max_val>")
def pok_by_attack(min_val: int, max_val: int):
    """Return all pokemons with attack in the specified range"""


@app.route("/defense/<int:min_val>/<int:max_val>")
def pok_by_defense(min_val: int, max_val: int):
    """Return all pokemons with defense in the specified range"""


@app.route("/type/<string:pok_type>")
def pok_by_type(pok_type: str):
    """Return all pokemons of the specified type"""


@app.route("/legendary")
def pok_by_status():
    """Return all legendary pokemons as HTML"""
