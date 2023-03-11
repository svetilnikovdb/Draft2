from selenium import webdriver
import pytest

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_example_homepage(browser):
    browser.get("https://www.example.com")
    assert "Example Domain" in browser.title
