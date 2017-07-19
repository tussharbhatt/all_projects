import time
from selenium import webdriver
# chromeDriver="C:\Program Files (x86)\Google\Chrome\Application"
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://dimensiondata.sabacloud.com/Saba/Web_spf/SPCTNT6Site/common/ledetail/00019176")
time.sleep(60)
# text="tussharbhatt@gmail.com"

try:
    elem = driver.find_element_by_id('splitbutton-1091-btnInnerEl')
    elem.click()
    elem.submit()

finally:
    print("hello")

try:
    # print
    "about to look for element"
    elem = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(".//*[@id='player-close-toolEl']"))
    # print
    # elem.click()
    "still looking?"
finally:
    elem.click()
    print("okk")

try:
    elem = WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element_by_xpath(".//*[@id='button-1115-btnIconEl']"))


finally:
    elem.click()
# elem=driver.find_element_by_xpath(".//*[@id='identifierId']")

# elem.send_keys(text)
# elem.find_element_by_class_name("RveJvd snByac")
# elem.click()
# elem.find_element_by_xpath(".//*[@id='password']/div[1]/div/div[1]/input")
# elem.send_keys(upass)
# elem.find_element_by_xpath(".//*[@id='passwordNext']/content/span")
# elem.click() '''
