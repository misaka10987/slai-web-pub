# Day 3: Interactivity

We add HTML form to the front of our application to interact with the logic (back-end).

## Learning goals

- Use various elements of HTML forms to retrieve subset of the dataset from the back-end of the application.
- Learn basics of HTTP methods.

## Process

New features added to the application:

1. Data exploration script returns a `list` of dictionaries with values converted to the proper types (`int`, `bool` etc).
2. Main route handles both `GET` and `POST` methods, rendering either a form or the resulting table.
3. A new function, `query`, is used to filter the results based on the form values.
4. HTML form with various types of `input`:
    - `select/option`, `checkbox`, `text`, `number`, `submit`.

## Demo

1. HTML form is used to interact with data and retrieve specific records.

## Student outcomes

Students should be able to:

1. Use HTML forms
2. Use `flask.request.form` to retrieve data submitted by users

## References

- [Getting started with the web - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web)
- [HTML: HyperText Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [HTTP request methods - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [Jinja — Jinja Documentation (3.1.x)](https://jinja.palletsprojects.com/en/3.1.x/)
- [MVP.css - Minimalist stylesheet for HTML elements](https://andybrewer.github.io/mvp/)
