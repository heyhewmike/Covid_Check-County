#!/usr/bin/python3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

# Get cdc_county url from https://covid.cdc.gov/covid-data-tracker/index.html#county-view?list_select_state=all_states&data-type=CommunityLevels
# /html/body/div[7]/div[2]/main/div[2]/div[3]/div/div[1]/div/table/tbody/tr[1]/td/div/div[1]/div[2]


cdc_county = "https://covid.cdc.gov/covid-data-tracker/index.html#county-view?list_select_state=Connecticut&data-type=CommunityLevels&list_select_county=9007"

options = Options()
options.add_argument( "--headless")
driver = webdriver.Firefox(options=options)
driver.get(str(cdc_county))
#community_level = driver.find_element("id", 'CCL_community_burden_level_integer')
community_level = driver.find_element("xpath", "/html/body/div[7]/div[2]/main/div[2]/div[3]/div/div[1]/div/table/tbody/tr[1]/td/div/div[1]/div[2]")
driver.close
print(str(community_level))