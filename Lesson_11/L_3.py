from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
sbis_site = 'https://saby.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    tabs = browser.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, "Должно быть 4 вкладки"

finally:
    browser.quit()