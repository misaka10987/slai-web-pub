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
    ...


@main.post("/")
def post_index():
    """Render the template with jokes"""
    # TODO: Implement this function
    ...


@main.errorhandler(404)
def not_found(error):
    """Handle 404 Not Found error"""
    # TODO: Implement this function
    ...
