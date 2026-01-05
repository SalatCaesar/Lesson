from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    browser.get(sbis_site)
    sleep(1)
    assert browser.current_url == sbis_site, 'Неверно открыт сайт'
    news_item = browser.find_element(By.CSS_SELECTOR, '.sbisru-h5.sbisru-Main-news')
    browser.execute_script("return arguments[0].scrollIntoView(true);", news_item)
    news_item.click()
finally:
    browser.quit()