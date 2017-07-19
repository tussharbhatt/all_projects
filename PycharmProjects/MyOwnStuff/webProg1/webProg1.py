'''import selenium
from selenium.webdriver.common import keys

browser = selenium.webdriver.Firefox()
browser.get("https://www.python.org")
elem = selenium.webdriver.find_element_by_id('id_search_field')
elem.clear()
elem.send_keys("tussharbhatt@gmail.com")
#elem.send_keys(keys.RETURN)
''' '''import os
path=None
path=os.path.abspath(path)
print(path)'''

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#import org.openqa.selenium.Keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#driver.get("https://www.google.co.in/")
#assert "Python" in driver.title
#elem =driver.find_element_by_xpath(".//*[@id='gb_70']")
#elem.send_keys("bangalore")
#elem.click()
driver.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
elem=driver.find_element_by_xpath(".//*[@id='identifierId']")
userpass="tusharbhatt101091"
elem.send_keys("tussharbhatt@gmail.com")
elem=driver.find_element_by_xpath(".//*[@id='identifierNext']/div[2]")
elem.click()
driver.implicitly_wait(10)
driver.get("https://accounts.google.com/signin/v2/challenge/pwd?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.co.in%2F&flowName=GlifWebSignIn&flowEntry=Identifier&TL=AHnYQLz5N_MDMcJHmXdq9onz9-BbfvXKtkQkw-T3PfPYl2n9KzB13WB2uPjqseDIP3wuWRni19oSVDP4fosABAXj0Pk0Lo7nlF_kk-OZm2blPWNpIp8KsHqsHFZ8oHKvDJlmnyScPY1uyUzrCUG0Ik3gj_eblXUV6A&cid=1&navigationDirection=forward")
elem=driver.find_element_by_class_name("whsOnd zHQkBf")
elem.send_keys(userpass)
elem.find_element_by_class_name("RveJvd snByac")
elem.click()
#elem.sendKeys(Keys.RETURN)
#elem.clear()
#elem.send_keys("pycon")

assert "No results found." not in driver.page_source

#driver.close()