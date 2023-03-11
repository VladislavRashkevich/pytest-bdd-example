"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/

Setup and cleanup are handled using hooks.
For a real test automation project, use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:

 - Firefox must be installed.

 - geckodriver must be installed and accessible on the system path.
"""

import pytest

from pytest_bdd import parsers, scenarios, given, then, when
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Conatants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Scenario

scenarios("../features/web.feature")

# Fixtures

@pytest.fixture
def browser():
    browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

# Given steps
@given('the DuckDuckGo home page is displayed', target_fixture="ddg_home")
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)

# Then steps
@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n{text}'))
def search_phrase(browser, text):
    print(text)
    search_input = browser.find_element(By.NAME, "q")
    search_input.send_keys(text + Keys.RETURN)

# Then steps
@then(parsers.parse('one of the results contains "{phrase}"'))
def result_have_one(browser, phrase):
    xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
    result = browser.find_elements(By.XPATH, xpath)
    assert len(result) > 0

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)

    links_div = browser.find_element(By.ID, 'links')
    assert len(links_div.find_elements(By.XPATH, '//div')) > 0

    # Check search phrase
    search_input = browser.find_element(By.NAME, 'q')
    assert search_input.get_attribute('value') == phrase








