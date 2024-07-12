#!/usr/bin/env python3
"""
Using pytest-flask to test the back end

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest


def test_index_get(client):
    """GET should work"""
    assert client.get("/").status_code == 200


def test_index_post(client):
    """POST without any data should trigger query defaults"""
    assert client.post("/").status_code == 200


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
def test_form_post_valid(client, language, category):
    """Various combinations of language/category should be handled"""
    assert (
        client.post("/", data=dict(language=language, category=category)).status_code
        == 200
    )


@pytest.mark.parametrize(
    "language, category",
    [
        ("en", "twister"),
        ("es", "chuck"),
        ("es", "twister"),
        ("it", "twister"),
    ],
)
def test_form_post_error(client, language, category):
    """Various combinations of language/category should be handled"""
    assert (
        client.post("/", data=dict(language=language, category=category)).status_code
        == 404
    )


if __name__ == "__main__":
    pytest.main(["-v", __file__])
