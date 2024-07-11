#!/usr/bin/env python3
"""
Routes testing

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import random
import sys

import pytest


def test_get_index_status(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_index_data(client):
    response = client.get("/")
    assert '<form action="/" method="post">' in response.text


def test_post_index_status(client):
    response = client.post(
        "/",
        data={
            "primary_type": "any",
        },
    )
    assert response.status_code == 200


def test_post_index_data(client):
    response = client.post(
        "/",
        data={
            "primary_type": "any",
        },
    )
    assert "<table>" in response.text


def test_get_details_status(client):
    for pok_id in range(1, 722):
        response = client.get(f"/{pok_id}")
        assert response.status_code == 200


def test_get_details_error_status(client):
    for _ in range(10):
        pok_id = random.randint(722, sys.maxsize)
        response = client.get(f"/{pok_id}")
        assert response.status_code == 404


@pytest.mark.parametrize(
    "pok_id, pok_name",
    [
        (1, "Bulbasaur"),
        (101, "Electrode"),
        (201, "Unown"),
        (301, "Delcatty"),
        (401, "Kricketot"),
        (501, "Oshawott"),
        (601, "Klinklang"),
        (701, "Hawlucha"),
    ],
)
def test_get_details_data(client, pok_id, pok_name):
    response = client.get(f"/{pok_id}")
    assert pok_name in response.text


if __name__ == "__main__":
    pytest.main(["-v", __file__])
