#!/usr/bin/env python3
"""
Serving `pyjokes` via templates

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import dotenv
from flask import Flask


def create_app():
    app = Flask(__name__)
    dotenv.load_dotenv(".flaskenv")
    app.config.from_prefixed_env()
    app.numbers = (1, 5, 10)
    app.languages = {
        "en": "English",
        "de": "German",
        "it": "Italian",
        "es": "Spanish",
    }
    app.categories = {
        "all": "All",
        "chuck": "Chuck Norris",
        "neutral": "Neutral",
        "twister": "Twister",
    }
    from joker.routes import main

    app.register_blueprint(main)
    return app
