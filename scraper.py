from bs4 import BeautifulSoup
import requests

url = 'https://data.texas.gov/dataset/Mixed-Beverage-Gross-Receipts/naix-2893/about_data'

page = requests.get(url)

soup = BeautifulSoup(page.text, features='html.parser')

# print(soup)

refined_soup = soup.find(class_='action-button-wrapper')
print(refined_soup.prettify())
next_soup = refined_soup.find(class_='info-pane')
# print(next_soup)