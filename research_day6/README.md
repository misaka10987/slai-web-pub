# Day 6. Using databases

Python comes with SQLite built-in but can work with many other Database Management Systems via connectors and adapters.

- SQLite3
- MySQL
- PostgreSQL
- MongoDB

## SQLite3

Built into Python. Simple yet powerful file-based database.

```python
import sqlite3

conn = sqlite3.connect("chinook.db")
cur = conn.cursor()
cur.execute("select * from artists limit 10")
rows = cur.fetchall()
print(rows)
```

## `records`

`records` is a library that can be used to connect to various databases.

```python
import records

db = records.Database("sqlite:///chinook.db")
rows = db.query("select * from artists")
print(rows)
```

## References

- [SQLite Home Page](https://www.sqlite.org/)
- [sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.12.4 documentation](https://docs.python.org/3/library/sqlite3.html)
- [A Beginner’s Guide to the True Order of SQL Operations – Java, SQL and jOOQ.](https://blog.jooq.org/a-beginners-guide-to-the-true-order-of-sql-operations/)
