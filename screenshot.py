from selenium import webdriver
import time
import img_util

url = "https://statiz.sporki.com/"
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
driver.get_screenshot_as_file("baseball.png")
img_util.fullpage_screenshot(driver, 'full_baseball.png')

driver.close()