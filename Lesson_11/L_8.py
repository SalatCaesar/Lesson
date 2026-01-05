from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
sbis_site = 'https://test.sbis.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    start_btn = browser.find_element(By.CSS_SELECTOR, '.sbis_ru-Banner-btn')
    start_btn.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[1])

finally:
    browser.quit()