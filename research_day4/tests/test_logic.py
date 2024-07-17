#!/usr/bin/env python3
"""
Logic testing

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import pytest
from plucky.logic import lucky_number


def test_lucky_number():
    """Random numbers within the range"""
    assert lucky_number(1, 6) in range(1, 7)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
