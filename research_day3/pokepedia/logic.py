#!/usr/bin/env python3
from flask import current_app


def query(form: dict):
    result = []
    hp_min = int(form.get("hp_min", -1))
    hp_max = int(form.get("hp_max", 1000))
    hp_range = range(hp_min, hp_max)
    for monster in current_app.data:
        if monster["Type 1"] != form["primary_type"]:
            continue
        if monster["Health"] not in hp_range:
            continue
        result.append(monster)

    return result
