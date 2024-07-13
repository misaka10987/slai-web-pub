#!/usr/bin/env python3
"""
Frontend form testing

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import subprocess

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    """Create the server fixture"""
    module.server = subprocess.Popen(["flask", "--app", "plucky", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Stop the server"""
    module.server.terminate()


def test_index(page: Page):
    """Main page"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    assert len(page.query_selector_all("#buttons >> input")) == 6


@pytest.mark.parametrize("number", [1, 2, 3, 4, 5, 6])
def test_buttons(page: Page, number):
    """Main page buttons"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.locator(f"#btn{number}").click()
    assert page.locator("#result").is_visible()


def test_about(page: Page):
    """About page"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/about")
    assert page.get_by_text("Meow").is_visible()


@pytest.mark.parametrize(
    "path",
    [
        "hello",
        "lucky",
        "cat",
    ],
)
def test_notfound(page: Page, path):
    """Not found paths"""
    page.set_default_timeout(TIMEOUT)
    page.goto(f"http://localhost:5000/{path}")
    assert page.get_by_text("Purr").is_visible()


if __name__ == "__main__":
    pytest.main(["-v", __file__])
