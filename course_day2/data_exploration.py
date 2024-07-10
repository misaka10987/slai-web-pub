#!/usr/bin/env python

import csv


def read_csv(filename: str):
    with open(filename) as f:
        return [record for record in csv.DictReader(f)]
