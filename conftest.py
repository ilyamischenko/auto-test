from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(
    level=logging.INFO,  # Устанавливаем минимальный уровень для логов
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщений лога
)


@pytest.fixture()
def browser():
    logging.info("Настраиваем браузер с параметрами")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Отключение GPU (полезно для Windows)

    logging.info("Запускаем браузер в headless-режиме с заданными опциями.")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    # browser.implicitly_wait(3)  селениум сразу после открытия не успевает найти элемент который ищу
    yield browser

    logging.info("Закрываем браузер.")

