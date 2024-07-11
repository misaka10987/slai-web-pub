#!/usr/bin/env python3
"""
Routes testing

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest
from pokepedia.logic import query


@pytest.mark.parametrize(
    "form, records",
    [
        (
            {
                "primary_type": "any",
                "secondary_type": "any",
                "generation": "any",
                "legendary": "off",
                "min_hp": "",
                "max_hp": "",
                "min_att": "",
                "max_att": "",
                "min_def": "",
                "max_def": "",
            },
            800,
        ),
        (
            {
                "primary_type": "Ghost",
            },
            32,
        ),
        (
            {
                "primary_type": "Ghost",
                "legendary": "on",
            },
            2,
        ),
        (
            {
                "min_hp": "0",
                "max_hp": "0",
            },
            0,
        ),
    ],
)
def test_query(app, form: dict, records: int):
    with app.app_context():
        assert len(query(form)) == records


if __name__ == "__main__":
    pytest.main(["-v", __file__])
