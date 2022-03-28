from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time 



PATH = "C:\Program Files (x86)\chromedriver.exe"


driver = webdriver.Chrome(PATH)
driver.get("https://login.proxy.bib.uottawa.ca/login?url=https://www.webofknowledge.com/wos")
driver.execute_script("shibAuth()")
driver.find_element_by_id("i0116").send_keys("pkumar2@uottawa.ca")
driver.find_element_by_id("idSIButton9").click()
driver.find_element_by_id("i0118").send_keys("Astayuno1129!")
time.sleep(1)
driver.find_element_by_xpath("//input[@value = 'Sign in']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@value = 'Yes']").click()
time.sleep(3)
driver.find_element_by_id("onetrust-accept-btn-handler").click()
time.sleep(1)
driver.find_element_by_id("pendo-close-guide-ecbac349").click()
time.sleep(1)
driver.find_element_by_link_text("RESEARCHERS").click()
time.sleep(3)
driver.find_element_by_id("mat-input-0").send_keys("Elias") # Last name field
driver.find_element_by_id("mat-input-1").send_keys("Ashley") # First name field
time.sleep(1)
driver.find_element_by_xpath("//button[@cdxanalyticscategory = 'WOS-authorsearch-search']").click()
# driver.find_element_by_xpath("").click()
time.sleep(3000)
driver.quit()
