#!/usr/bin/env python

import csv


def read_csv(filename: str):
    with open(filename) as f:
        return [monster for monster in csv.DictReader(f)]
