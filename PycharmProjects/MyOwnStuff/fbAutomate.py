from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = "tussharbhatt"
pwd = "tusharbhatt101091"
driver = webdriver.Firefox()
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
#elem.send_keys(Keys.RETURN)
elem=driver.find_element_by_xpath(".//*[@id='u_0_q']")
elem.click()
elem=driver.find_element_by_class_name("q")
elem.send_keys("devansh bhatt")
elem.submit()
#elem.click()
#driver.close()