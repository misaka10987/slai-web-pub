#!/usr/bin/env python3
"""
Flask app logic

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import random


def lucky_number(a: int, b: int) -> int:
    """
    Generate a random number within certain range
    """
    return random.randint(a, b)
