from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import getpass

# EMAIL = input("Username: ")
# PASSWORD = getpass.getpass()
# FNAME = "Ashley"
# LNAME = "Elias"
# COUNT = 0

PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "https://login.proxy.bib.uottawa.ca/login?url=https://www.webofknowledge.com/wos"

class WOS_data_collector:
    def __init__(self,driver_path, driver_setings = None):
        '''
            Function to generate a new web driver.
            Parameters
            ----------
            driver_path - The local file path where the driver file is located
            driver_setings - the configuration for the driver

            Returns
            -------
            driver - A webdriver used to communicate with the chrome browser

        '''
        if driver_setings == None:
            self.driver = webdriver.Chrome(executable_path = driver_path)
        else:
            self.driver = webdriver.Chrome(executable_path = driver_path, desired_capabilities = driver_setings)


    def login_to(self,web_url,email,password):
        '''
            Function to login into Web of Sciecne (WOS) using the given credentials.
            Parameters
            ----------
            driver - A webdriver used to communicate with the chrome browser
            web_url- URL to establish connection with
            email - Username for WOS login
            password - Password for WOS login

            Returns
            -------
            Web of science page is opened and logged in with the given credentials

        '''
        self.driver.get(web_url)
        self.driver.execute_script("shibAuth()")
        self.driver.find_element_by_id("i0116").send_keys(email)
        self.driver.find_element_by_id("idSIButton9").click()
        self.driver.find_element_by_id("i0118").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value = 'Sign in']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@value = 'Yes']").click()
        time.sleep(3)
        self.driver.find_element_by_id("onetrust-accept-btn-handler").click()
        time.sleep(1)
        self.driver.find_element_by_id("pendo-close-guide-ecbac349").click()
        time.sleep(1)

    def search_and_download(self,fname,lname):
        '''
            Function to search and download given authors citation report.
            Parameters
            ----------
            driver - A webdriver used to communicate with the chrome browser
            fname - First name of the author
            lname - Last name of the author

            Returns
            -------
            Excel form of citation report of the author saved to local disk

        '''
        # global COUNT
        self.driver.find_element_by_link_text("RESEARCHERS").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@formcontrolname = 'lastName']").send_keys(Keys.CONTROL+"A",Keys.DELETE)
        self.driver.find_element_by_xpath("//input[@formcontrolname = 'lastName']").send_keys(lname) # Last name field
        self.driver.find_element_by_xpath("//input[@formcontrolname = 'firstName']").send_keys(Keys.CONTROL+"A",Keys.DELETE)
        self.driver.find_element_by_xpath("//input[@formcontrolname = 'firstName']").send_keys(fname) # First name field
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@cdxanalyticscategory = 'WOS-authorsearch-search']").click()
        time.sleep(4)
        # if COUNT ==2:
        #     driver.find_element_by_xpath("//button[@class= '_pendo-close-guide']").click()
        self.driver.find_element_by_partial_link_text(lname).click()
        time.sleep(1)
        self.driver.find_element_by_link_text('View citation report').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label = 'Export Full Report']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@data-placeholder = 'File name']").send_keys(fname+" "+lname)
        time.sleep(1)
        self.driver.find_element_by_xpath("//mat-radio-button[@value = 'crx']").click()
        self.driver.find_element_by_xpath("//button[@class = 'standard-button primary-button']").click()
        # COUNT = COUNT+1
        time.sleep(1)
        self.driver.find_element_by_link_text('Search').click()
    
    def quit_session(self):
        '''
            Function to quit web browser session.
            Parameters
            ----------
            driver - A webdriver used to communicate with the chrome browser

            Returns
            -------
            Quits the browser session

        '''    
        self.driver.quit()

# driver = WOS_data_collector(PATH)
# driver.login_to(URL,EMAIL,PASSWORD)
# driver.search_and_download(FNAME,LNAME)
# driver.quit_session()