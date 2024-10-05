from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Добавляем webdriver_manager для ChromeDriver
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
    options.add_argument('--no-sandbox')  # Безопасный режим (полезно для CI/CD)
    options.add_argument('--disable-dev-shm-usage')  # Исправляет проблемы с памятью на серверах

    logging.info("Запускаем браузер с webdriver_manager.")

    # Автоматическая установка ChromeDriver с помощью webdriver_manager
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)

    yield browser

    logging.info("Закрываем браузер.")
    browser.quit()
