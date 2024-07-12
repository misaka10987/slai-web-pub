#!/usr/bin/env python3

from flask import Flask, render_template, current_app
from loader import load


def create_app():
    app = Flask(__name__)
    app.data = load("./static/table.csv")
    return app


app = create_app()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<int:a_num>")
def by_atomic_number(a_num: int):
    return render_template("element.html", element=current_app.data[a_num])

@app.route("/table")
def show_table():
    return render_template("table.html", data=current_app.data)
