# selenium test

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')  # Optional argument, if not specified will search path.
#driver.get('http://www.google.com/xhtml')

driver.get('http://www.facebook.com')
time.sleep(5)

'''driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source'''
driver.close()
