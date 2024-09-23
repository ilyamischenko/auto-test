import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser




def test_open_sg_s6(browser):
    browser.get('https://www.demoblaze.com/')

