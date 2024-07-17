#!/usr/bin/env python3

import pyjokes
import random
from flask import abort


def query(lang: str = "en", cat: str = "all", num: str = "1") -> list[str]:
    """Return a list of jokes

    param language: selected language
    param category: selected category
    param number: selected number of jokes

    returns: list of random jokes in the chosen language/category with at most `number` of items
    """
    # TODO: Implement this function
    res = pyjokes.get_jokes(lang, cat)
    random.shuffle(res)
    return res[0 : min(len(res), int(num))]
    # return [pyjokes.get_joke(lang, cat) for _ in range(0, int(num))]
