from itertools import product
from requests import options
import time
from pages.homepage import HomePage
from pages.product import ProductPage



def test_open_sg_s6(browser):

    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')



def test_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    time.sleep(5)
    homepage.quantity_monitors(2)
    # browser.get('https://www.demoblaze.com/')
    # monitor_link = browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    # monitors = browser.find_elements(By.CSS_SELECTOR, '.card')
    # assert len(monitors) == 2
#     с помощью len узнаем количество списка monitors
