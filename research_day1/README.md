# Day 1: `Flask` routes and return types

We look at `Flask` routing and variable rules.

## Goals

- Review Flask routing rules.
- Use converters with variable rules.
- Return any data as JSON or HTML (using `Response`).
- Handle basic errors without crashing the application.
- Use `curl` or a similar tool to interact with the application.
- Use Python built-in string templates.

## Outcomes

`Flask` application with the following functionality:

- Return some information about records in the file as HTML
  - filter by id
  - filter by the legendary status
- Return some information about records in the file as JSON
  - filter by id
  - filter by attack range
  - filter by defense range
  - filter by type
- Handle simple error cases
  - misspelled name
  - invalid range
  - misspelled type

Using `curl` or the Visual Studio Code extension you should be able to retrieve data from the application.

```bash
curl http://localhost:5000/api/Pikachu
```

## References

- [Flask 3.0 documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [Pokemon dataset](https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6)
- [Python template strings](https://docs.python.org/3/library/string.html#template-strings)  
