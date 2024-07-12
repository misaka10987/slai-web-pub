#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import sys

import pytest
from joker.logic import query


@pytest.mark.parametrize(
    "language, category",
    [
        ("de", "all"),
        ("de", "chuck"),
        ("de", "neutral"),
        ("de", "twister"),
        ("en", "all"),
        ("en", "chuck"),
        ("en", "neutral"),
        ("es", "all"),
        ("es", "neutral"),
        ("it", "all"),
        ("it", "chuck"),
        ("it", "neutral"),
    ],
)
def test_query(language, category):
    """Various combinations of language/category should be handled"""
    assert len(query(language, category)) == 1


@pytest.mark.parametrize(
    "language, category",
    [
        ("en", "twister"),
        ("es", "chuck"),
        ("es", "twister"),
        ("it", "twister"),
    ],
)
def test_query_error(language, category):
    """Not all combinations are valid"""
    assert len(query(language, category)) == 0


@pytest.mark.parametrize(
    "language, category, number",
    [
        ("de", "all", 146),
        ("de", "chuck", 68),
        ("de", "neutral", 59),
        ("de", "twister", 19),
        ("en", "all", 200),
        ("en", "chuck", 103),
        ("en", "neutral", 97),
        ("en", "twister", 0),
        ("es", "all", 14),
        ("es", "chuck", 0),
        ("es", "neutral", 14),
        ("es", "twister", 0),
        ("it", "all", 159),
        ("it", "chuck", 87),
        ("it", "neutral", 72),
        ("it", "twister", 0),
    ],
)
def test_query_number(language, category, number):
    """
    There is a limited number of jokes in each category/language.
    Requesting infinity (sys.maxsize) should return all jokes of that combination
    """
    assert len(query(language, category, sys.maxsize)) == number


if __name__ == "__main__":
    pytest.main(["-v", __file__])
