#!/usr/bin/env python3
"""
Frontend form testing

@authors: Roman Yasinovskyy
@version: 2024.7
"""

# import os
import subprocess

import pytest
from playwright.sync_api import Page

TIMEOUT = 1000


def setup_module(module):
    """Create the server fixture"""
    # os.chdir("research_day3")
    module.server = subprocess.Popen(["flask", "--app", "pokepedia", "run"])
    try:
        module.server.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass


def teardown_module(module):
    """Stop the server"""
    module.server.terminate()


def test_default_query(page: Page):
    """Click a button without selecting any options"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.click("#btnQuery")
    assert len(page.query_selector_all("table > tbody > tr")) == 800


def test_selected_primary_type(page: Page):
    """Select primary type"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#primary_type", "Ghost")
    page.click("#btnQuery")
    assert len(page.query_selector_all("table > tbody > tr")) == 32


def test_selected_primary_type_legendary(page: Page):
    """Select primary type and legendary status"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.select_option("#primary_type", "Ghost")
    page.check("#legendary")
    page.click("#btnQuery")
    assert len(page.query_selector_all("table > tbody > tr")) == 2


def test_health(page: Page):
    """Enter health range"""
    page.set_default_timeout(TIMEOUT)
    page.goto("http://localhost:5000/")
    page.locator("#min_hp").fill("0")
    page.locator("#max_hp").fill("0")
    page.click("#btnQuery")
    assert len(page.query_selector_all("table > tbody > tr")) == 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])
