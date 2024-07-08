# Day 0: Data formats

We review of Python through the process of handling data in various formats.

Original data is a list [ACM member colleges](https://en.wikipedia.org/wiki/Associated_Colleges_of_the_Midwest) including each member's name, city, and state.

## Goals

- Python syntax
  - *Pythonic* code patterns
  - f-strings
- Collections (`list` and `dict`)
  - `list` comprehensions
- Working with files using context manager and `pathlib`
- Standard library modules
  - `json`
  - `tomllib`
  - `xml`
- General code organization and handling command-line arguments using `argparse`

## Outcomes

An application with the following functionality:

- reads data in various formats
  - `text`
  - `json`
  - `toml`
  - `xml`
- displays the resulting subset of the original data
- consistent formatting of the output
- consistent API

The application should be invoked with two parameters, name of the input file and the filter (state):

```bash
>> python acm.py acm.txt --state IA
```

The expected output is as follows:

```text
Looking for Iowa ACM colleges in the file acm.txt
College                  State          City           
-------------------------------------------------------
Coe College              Iowa           Cedar Rapids   
Cornell College          Iowa           Mount Vernon   
Grinnell College         Iowa           Grinnell       
Luther College           Iowa           Decorah 
```

## References

- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [tomllib — Parse TOML files](https://docs.python.org/3/library/tomllib.html)
- [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [XML Processing Modules](https://docs.python.org/3/library/xml.html)
