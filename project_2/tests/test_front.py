#!/usr/bin/env python3
"""
Using pytest-playwright to test the front end

@authors: Roman Yasinovskyy
@version: 2024.7
"""

import subprocess

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    """Create the server fixture"""
    module.server = subprocess.Popen(["flask", "--app", "joker", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Stop the server"""
    module.server.terminate()


def test_click_button(page: Page):
    """Click a button without selecting any category/language"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.click("#button_query")
    assert len(page.query_selector_all("#jokes > p")) == 1


@pytest.mark.parametrize("number", [1, 5, 10])
def test_select_number(page: Page, number):
    """Select different number of jokes"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#select_number", str(number))
    page.click("#button_query")
    assert len(page.query_selector_all("#jokes > p")) == number


@pytest.mark.parametrize("language", ["de", "en", "es", "it"])
def test_select_language(page: Page, language):
    """Select different languages"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#select_language", language)
    page.click("#button_query")
    assert len(page.query_selector_all("#jokes > p")) == 1


@pytest.mark.parametrize("category", ["all", "chuck", "neutral"])
def test_select_category(page: Page, category):
    """Select different categories"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#select_category", category)
    page.click("#button_query")
    assert len(page.query_selector_all("#jokes > p")) == 1


def test_select_twister(page: Page):
    """Twisters are only available in German"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#select_category", "twister")
    page.select_option("#select_language", "de")
    page.click("#button_query")
    assert len(page.query_selector_all("#jokes > p")) == 1


@pytest.mark.parametrize(
    "language, category",
    [
        ("en", "twister"),
        ("es", "chuck"),
        ("es", "twister"),
        ("it", "twister"),
    ],
)
def test_select_chuck_in_spanish(page: Page, language, category):
    """There are no jokes about Chuck Norris in Spanish"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#select_category", category)
    page.select_option("#select_language", language)
    page.click("#button_query")
    assert len(page.query_selector_all("#jokes > p")) == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
