from selenium import webdriver
import pytest



@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    # browser.implicitly_wait(3)  селениум сразу после открытия не успевает найти элемент который ищу
    yield browser