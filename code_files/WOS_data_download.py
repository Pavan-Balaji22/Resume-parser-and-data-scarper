from WOS_data_collector import WOS_data_collector as wdc
import getpass

EMAIL = input("Username: ")
PASSWORD = getpass.getpass()
FNAME = "Ashley"
LNAME = "Elias"
PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = "https://login.proxy.bib.uottawa.ca/login?url=https://www.webofknowledge.com/wos"

driver = wdc(PATH)
driver.login_to(URL,EMAIL,PASSWORD)
driver.search_and_download(FNAME,LNAME)
driver.quit_session()