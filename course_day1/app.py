#!/usr/bin/env python3
from flask import Flask
from data_exploration import read_csv

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, SLAI web developers!"


@app.route("/<int:pok_id>")
def pok_by_id(pok_id):
    data = read_csv("pokemon.csv")
    return ...
