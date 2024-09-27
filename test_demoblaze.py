import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from unicodedata import category
import  time


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    # browser.implicitly_wait(3)  селениум сразу после открытия не успевает найти элемент который ищу
    yield browser




def test_open_sg_s6(browser):
    browser.get('https://www.demoblaze.com/')
    galaxy_s6 = browser.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div[1]/div[1]/h4[1]/a[1]')
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text == 'Samsung galaxy s6'


def test_monitors(browser):
    browser.get('https://www.demoblaze.com/')
    monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(5)
    monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors) == 2
#     с помощью len узнаем количество списка monitors
