import os

import pytest

from pytest_bdd import given, when



pytest_plugins = "pytester", "splinter"

@pytest.fixture
def pytestbdd_feature_base_dir():
    return os.path.join(os.path.dirname(__file__), 'features/')


@given("I open the example project")
def open_example_project(browser):
    browser.visit("http://127.0.0.1:9000")


@when("I go to the homepage")
def open_homepage(browser):
    open_example_project(browser)


@when("I submit the form")
def submit_form(browser):
    browser.find_by_xpath('//input[@type="submit"]').click()
