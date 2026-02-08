from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    toolbar = browser.find_element(By.CSS_SELECTOR, '.sbisru-Header__button')
    toolbar.click()
finally:
    browser.quit()