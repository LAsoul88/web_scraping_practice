from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Firefox(options=options)
url = 'https://data.texas.gov/dataset/Mixed-Beverage-Gross-Receipts/naix-2893/about_data'
driver.get(url)

button = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[2]/div/div/div/forge-button/button').click()
download = driver.find_element(By.XPATH, '/html/body/forge-dialog/div/forge-scaffold/div[3]/forge-toolbar/forge-button[2]/button').click()
# print(download)
# driver.quit()

# page = requests.get(url)

# soup = BeautifulSoup(page.text, features='html.parser')

# print(soup)

# refined_soup = soup.find(class_='action-button-wrapper')
# print(refined_soup.prettify())
# next_soup = refined_soup.find(class_='info-pane')
# print(next_soup)