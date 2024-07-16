#!/usr/bin/env python3
"""Working with records"""

import sqlite3

import records


def read_natively(db_name: str, table: str) -> None:
    """Read all records"""
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table};")
        for artist in cursor:
            print(artist)


def read_with_records(db_name: str, table: str) -> None:
    """Query records"""
    db = records.Database(f"sqlite:///{db_name}")
    rows = db.query(f"SELECT * FROM {table};")
    for artist in rows:
        print(artist)


def main():
    """Main function"""
    read_natively("chinook.db", "artists")
    read_with_records("chinook.db", "artists")


if __name__ == "__main__":
    main()
