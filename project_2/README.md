# Project 2: Just kidding

Use `Flask` and [pyjokes](https://github.com/pyjokes/pyjokes) to build a web application that would allow users to select language and category of a joke and use `Jinja` to print the specified number of jokes from the selected category.

```python
>>> import pyjokes
>>> pyjokes.get_joke()
>>> pyjokes.get_jokes()
>>> pyjokes.get_jokes(language="de", category="neutral")
```

 Note that there are some discrepancies between the released package (0.6.0 released in 2019) and the one on GitHub.
 Over the years the package expanded considerably and added  many languages but those changes have not been released yet.

## Requirements

1. Use any HTML/CSS framework to style the app.
2. Use `select` element to choose the joke language (_de_, _en_, _es_, or _it_).
3. Use `select` element to choose the joke category (_all_, _neutral_, or _chuck_).
4. Use `select` element to choose the number of jokes (1, 5, and 10).
5. Populate options of the `select` elements using `Jinja` templates.
6. Call `pyjokes.get_jokes()` to retrieve multiple jokes at once.
7. Handle errors (e.g. there are no Chuck Norris jokes in Spanish, twisters are only available in German etc) gracefully and return `404 Not Found` if necessary.
8. Pass the provided tests.

### _\_\_init\_\__.py

Initialization of the application, including secret key (should you need it) is done.
You don't have to change this file unless you want to.

### _logic.py_

Function `query` takes three arguments (`language`, `category`, and `number`) and returns a list with **at most** the requested number of jokes in the chosen language/category combination.
The function must return an empty list if either `pyjokes.pyjokes.LanguageNotFoundError` or `pyjokes.pyjokes.CategoryNotFoundError` is caught.

### _routes.py_

There is basically a single route, `/`, with two methods, `get` and `post` used to access it.
If the request method is `get`, present the form. Options `languages`, `categories`, and `numbers` for the `select` elements are initialized by the `create_app` function in the provided _\_\_init\_\_.py_.
If the request method is `post`, collect the selected options from the HTML form and render the _index.html_ template with the jokes returned by `query`.
If there are no jokes that match the language/category criteria (i.e. `query` returns an empty list) abort the application with the HTTP code `404 Not Found`.

### _index.html_

General layout of the page is up to you and some etails depend on the chosen framework but the following elements and their `id` are required:

- button `#button_query` that submits a `post` request to `/`.
- drop-down named `number` with id `select_number` that allows use pick the number of jokes.
- drop-down named `category` with id `select_category` that allows use pick the category of jokes.
- drop-down named `language` with id `select_language` that allows use pick the language of jokes.
- section with id `jokes` that contains jokes with each joke wrapped in a paragraph tag `p`.

## Testing

Use the provided tests to verify the correctness of implementation.

```bash
python3 -m pytest -v test_logic.py
python3 -m pytest -v test_routes.py
python3 -m pytest -v test_front.py
```

**Important**: the front-end testing relies heavily on the structure of the page an you must implement it exactly for `playwright` to find the page elements (drop-downs, the button, and the resulting section full of jokes.)

Once the application is finished you should run all test together:

```bash
python3 -m pytest -v tests
```

## References

- [pyjokes](https://pyjok.es/)
- [pyjokes/pyjokes: One line jokes for programmers (jokes as a service)](https://github.com/pyjokes/pyjokes)
