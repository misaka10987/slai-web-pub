#!/usr/bin/env python3

import csv
from pprint import pprint


def read_csv(filename):
    with open(filename, "r") as f:
        return [monster for monster in csv.DictReader(f)]


pprint(read_csv("pokemon.csv"))
