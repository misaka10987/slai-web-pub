#!/usr/bin/env python3
"""
Routes testing

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest


def test_get_index_status(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_index_data(client):
    response = client.get("/")
    assert "make a guess" in response.text


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6])
def test_post_index_status(client, number):
    response = client.post("/", data={"guess": str(number)})
    assert response.status_code == 200


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6])
def test_post_index_data(client, number):
    response = client.post("/", data={"guess": str(number)})
    assert "result" in response.text


def test_about_status(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_about_data(client):
    response = client.get("/about")
    assert "Meow!" in response.text


@pytest.mark.parametrize(
    "path",
    [
        "hello",
        "lucky",
        "cat",
    ],
)
def test_notfound_status(client, path):
    response = client.get(f"/{path}")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "path",
    [
        "hello",
        "lucky",
        "cat",
    ],
)
def test_notfound_data(client, path):
    response = client.get(f"/{path}")
    assert "Purr" in response.text


if __name__ == "__main__":
    pytest.main(["-v", __file__])
