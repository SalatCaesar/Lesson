from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
sbis_site = 'https://test.sbis.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    start_btn = browser.find_element(By.CSS_SELECTOR, '.sbisru-Button--primary')
    start_btn.click()
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('my_login')
    login.clear()

finally:
    browser.quit()