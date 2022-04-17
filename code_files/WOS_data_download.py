from WOS_data_collector import WOS_data_collector as wdc
import getpass
from selenium.webdriver import ChromeOptions
import os
import pandas as pd

EMAIL = "pkumar2@uottawa.ca" # input("Username: ")
PASSWORD = "Astayuno1129!" #getpass.getpass()
# FNAME = "Ashley"
# LNAME = "Elias"
PATH = "C:\chromedriver.exe"
cwd = os.getcwd()
URL = "https://login.proxy.bib.uottawa.ca/login?url=https://www.webofknowledge.com/wos"

chromeOptions = ChromeOptions()
prefs = {"download.default_directory" : cwd +"\\WOS Files"}
chromeOptions.add_experimental_option("prefs",prefs)

def initiate_download(NAME,URL,EMAIL,PASSWORD,chromeOptions):
    err_names = list()
    for i in NAME["Name"]:
        FNAME,LNAME = extract_name(i)
        driver = wdc(PATH,chromeOptions)
        driver.login_to(URL,EMAIL,PASSWORD)
        try:
            driver.search_and_download(FNAME,LNAME)
        except:
            try:
                driver.search_and_download(FNAME,LNAME,i)
            except:
                err_names.append(i)
            
        driver.quit_session()
    return err_names
def extract_name(i):
    temp = i.split()
    FNAME = temp[0]
    LNAME =  temp[-1]
    return FNAME.capitalize(),LNAME.capitalize()




Names = pd.read_csv("Name.csv")
un_names=initiate_download(Names,URL,EMAIL,PASSWORD,chromeOptions)
un_names = pd.DataFrame(un_names).T
un_names.to_json("error_names.json")