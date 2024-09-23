from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
urls = ["https://www.tiktok.com/explore"]

options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")

print('thusly')
driver = webdriver.Firefox(options=options)
print('here')
driver.get(urls[0])
print(driver)
singing_and_dancing = driver.find_element(By.XPATH, '/html/body/div/div')
print(singing_and_dancing)
singing_and_dancing.find_element(By.XPATH, 'div')
driver.quit()
# while len(urls) > 0:
#   current_url = urls.pop()

#   response = requests.get(current_url)
#   soup = BeautifulSoup(response.content, "html.parser")
#   print(soup)

#   button_elements = soup.select("button")
#   print(button_elements)
#   for button in button_elements:
#     url = button['href']
#     if "https://www.tiktok.com/" in url:
#       urls.append(url)

# print(urls)



# button = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/div/div[2]/div/div/div/forge-button/button').click()
# download = driver.find_element(By.XPATH, '/html/body/forge-dialog/div/forge-scaffold/div[3]/forge-toolbar/forge-button[2]/button').click()
# print(download)
# driver.quit()

# page = requests.get(url)

# soup = BeautifulSoup(page.text, features='html.parser')

# print(soup)

# refined_soup = soup.find(class_='action-button-wrapper')
# print(refined_soup.prettify())
# next_soup = refined_soup.find(class_='info-pane')
# print(next_soup)