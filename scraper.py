from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
urls = ["https://www.tiktok.com/explore"]

# options = webdriver.FirefoxOptions()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Firefox(options=options)
driver = webdriver.Chrome()
driver.get(urls[0])

try:
  driver.implicitly_wait(2)
  singing_and_dancing = driver.find_element(By.XPATH, '//*[@id="main-content-explore_page"]/div/div[1]/div/button[2]')
  singing_and_dancing.click()
  
  videos = driver.find_element(By.XPATH, '//*[@id="main-content-explore_page"]/div/div[2]/div/div[1]/div[1]/div/div/a/div/div[1]/div/span/picture')

  first_vid = videos.find_element(By.XPATH, '//img')
  driver.implicitly_wait(2)
  print(first_vid)
  driver.execute_script("arguments[0].click();", first_vid)
  driver.implicitly_wait(4)
  song = driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/h4/a/div')
  print(song.text)

  
except Exception as e:
  print(e)

# driver.quit()
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