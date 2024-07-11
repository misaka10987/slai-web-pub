#!/usr/bin/env python3
from flask import current_app


def get_or(form: dict, key: str, fallback: int) -> int:
    res = form.get(key, fallback)
    if not res:
        return int(fallback)
    return int(res)


def query(form: dict):
    hp_min = get_or(form, "min_hp", 0)
    hp_max = get_or(form, "max_hp", 1000)
    hp_rng = range(hp_min, hp_max)

    def f_tp(monster):
        return True

    tp_1 = form.get("primary_type")
    if tp_1 is not None and tp_1 != "any":

        def f_tp(monster):
            return monster["Type 1"] == tp_1

    def f_gen(monster):
        return True

    gen = form.get("generation")
    if gen is not None and gen != "any":

        def f_gen(monster):
            return monster["Generation"] == int(gen)

    legend = form.get("legendary", "off")
    legend = legend == "on"

    result = [
        monster
        for monster in current_app.data
        if f_tp(monster)
        and f_gen(monster)
        and monster["Health"] in hp_rng
        and (not legend or monster["Legendary"])
    ]

    return result
