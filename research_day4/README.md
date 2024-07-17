# Day 4: All together now

## Goals

- Develope a small application that uses all components we've seen previously.

## Outcomes

An application with the following functionality:

- Back-end is broken into 3 components:
  - initialization
  - routes
  - logic
- Front-end includes the following pages:
  - Main form(s)
  - Results
  - About page
  - Not found template
- Clicking a button sends a `POST` request to the application
- All parts of the application are tested using `pytest` and `playwright`

## Demo

Use the following command to run the application:

```bash
flask --app plucky run
```

Use the following command to test the application:

```bash
python -m pytest -v tests
```

## References

- [Getting started with the web - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web)
- [HTML: HyperText Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Jinja — Jinja Documentation (3.1.x)](https://jinja.palletsprojects.com/en/3.1.x/)
- [Bootstrap · The most popular HTML, CSS, and JS library in the world.](https://getbootstrap.com/)
