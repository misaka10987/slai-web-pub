#!/usr/bin/env python3
"""
Geography query app

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    render_template,
    request,
)

from geography.logic import read_db

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index() -> str:
    """Display selection form"""
    return render_template(
        "index.html",
        countries=current_app.countries,
        regions=current_app.regions,
        continents=current_app.continents,
    )


@main.post("/")
def post_index() -> str:
    """Handle selection

    Build a query based on the form and supply this query to `logic.read_db`
    """
    # TODO: Implement this function
    ...

    form = request.form
    key = [key for key in form.keys()]
    value = [value for value in form.values()]
    print(key, value)
    if len(key) != 1 or len(value) != 1:
        abort(400)
    key, value = key[0], value[0]

    print(key, value)
    
    filters = {
        "country": "name",
        "region": "subregion",
        "continent": "continental_region"
    }
    
    query = f"SELECT name as country_name, continental_region, subregion, capital, area, population_2023 as population, government_system, executive_head,  FROM country WHERE {filters[key]} = ?"
    
    result = read_db(query, (value,))

    print(result)

    return render_template(
        "index.html",
        data=result,
    )


@main.errorhandler(404)
def not_found(error):
    return render_template("index.html", error=error), 404


@main.context_processor
def add_select_options():
    return {
        "countries": current_app.countries,
        "regions": current_app.regions,
        "continents": current_app.continents,
    }
