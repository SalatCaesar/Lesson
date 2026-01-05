from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
sbis_site = 'https://saby.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    start_btn = browser.find_element(By.CSS_SELECTOR, '.sbisru-Main-banner-img')
    title = start_btn.get_attribute('title')
    assert title == 'Начать работать'

finally:
    browser.quit()