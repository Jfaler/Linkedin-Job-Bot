"""
Author: Justin Faler
Description: Apply to LinkedIn Jobs.
"""
import time, os, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options as Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

#options = Options()
#options.add_argument("--headless")

print(r"""
                                   ._ o o
                                   \_`-)|_
                                ,""       \
                              ,"  ## |   ಠ ಠ.
                            ," ##   ,-\__    `.
                          ,"       /     `--._;)
                        ,"     ## /
                      ,"   ##    /
                
                Welcome to the LinkedIn Job Bot!
                Author: Justin Faler
                
                """)


email = input("Please enter your e-mail: ")
password = input("Please enter your password: ")
keywords = input("Please enter some job keywords: ")
location = input("Please enter a job location: ")

# This will select the highest value for the results per page
driver = webdriver.Firefox()#options=options)
driver.get("https://www.linkedin.com/login")

# login into linkedin
login = driver.find_element_by_name('session_key')
login.clear()
login.send_keys(email)

pw = driver.find_element_by_name('session_password')
pw.clear()
pw.send_keys(password)
pw.submit()

time.sleep(7)

# go to Jobs
jobs = driver.find_element_by_link_text('Jobs')
jobs.click()

time.sleep(5)

# job keywords
search = driver.find_elements_by_css_selector(".jobs-search-box__text-input")
search[0].clear()
search[0].send_keys(keywords)

# job location
search[2].clear()
search[2].send_keys(location)
search[2].send_keys(Keys.RETURN)

time.sleep(7)

# apply filters
check_filters = driver.find_element_by_xpath("//button[@data-control-name='all_filters']")
check_filters.click()
time.sleep(2)

# find easily apply button
easily_apply = driver.find_element_by_xpath("//label[@for='linkedinFeatures-f_AL']")
easily_apply.click()

time.sleep(1)

checkmarck_filter = driver.find_element_by_xpath("//button[@class='search-advanced-facets__button--apply ml4 mr2 artdeco-button artdeco-button--3 "
            "artdeco-button--primary ember-view']")
checkmarck_filter.click()
