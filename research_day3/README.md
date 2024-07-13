# Day 3: Testing frameworks

We reorganize our application to break it into separate components that can be be updated and tested individually.

## Learning goals

- Learn basics of unit testing.
- Start using test-driven development.

## Process

Install the following Python packages:

- `pytest`: general-purpose testing framework
- `playwight`: front-end testing framework
- `pytest-playwright`: a plugin to connect the two

Use the following command to install the required packages inside your virtual environment:

```bash
python -m pip install pytest playwright pytest-playwright
```

Install the required browsers for `playwright to use:

```bash
playwright install
```

New features added to the application:

1. The application resides in its own directory, _pokepedia_, separate from tests.
2. Application created and initialized in a separate file, _\_\_init.py\_\__.
3. Logic of the application is extracted into _logic.py_.
4. Routes are specified and handled in _routes.py_.
5. Every part of the application is tested to perform as expected.

## Demo

1. HTML form is used to interact with data and retrieve specific records.
2. Unit tests are used to verify proper functionality of every part of the application.

## Student outcomes

Students should be able to:

1. Improve the application functionality.
2. Use `pytest` and `playwright` to test the application.

## References

- [Get Started - pytest documentation](https://docs.pytest.org/en/8.2.x/getting-started.html)
- [Installation | Playwright Python](https://playwright.dev/python/docs/intro)
