# Day 2: HTML/CSS frameworks

## Goals

- Start using a class-based HTML/CSS framework.

## Outcomes

An application with the following functionality:

- Data presented on the web in a consistent manner using `Jinja` templates and a common class-based framework, Bootstrap or Bulma.
- CSS class and color are used to highlight legendary pokemons
  - _Legendary_ column is redundant and should not be visible with this approach.
- Framework-specific grid approach is used to display pokemon details.
- Pokemon details should not include the following:
  - `ID` (not part of the statistics)
  - `Name` (part of the page title)
  - `Legendary` (part of the page title)
  - `Type 2` (if empty, include it otherwise)

## Ideas

1. Main page (table view) is almost identical regardless of the chosen framework with minor differences in class names.
2. Design of the detailed view is open but the page must use either `container/row/col` (Bootstrap) or `grid/cell` (Bulma) approach.

## References

- [Getting started with the web - Learn web development | MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web)
- [HTML: HyperText Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [HTML Tutorial](https://www.w3schools.com/html/)
- [HTML Standard](https://html.spec.whatwg.org/)
- [CSS: Cascading Style Sheets | MDN](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [CSS Tutorial](https://www.w3schools.com/css/)
- [CSS Snapshot 2023](https://www.w3.org/TR/css-2023/)
- [Jinja — Jinja Documentation (3.1.x)](https://jinja.palletsprojects.com/en/3.1.x/)
- [MVP.css - Minimalist stylesheet for HTML elements](https://andybrewer.github.io/mvp/)
- [Bootstrap · The most popular HTML, CSS, and JS library in the world.](https://getbootstrap.com/)
- [Bulma: Free, open source, and modern CSS framework based on Flexbox](https://bulma.io/)
- [troxler/awesome-css-frameworks: List of awesome CSS frameworks in 2024](https://github.com/troxler/awesome-css-frameworks)
