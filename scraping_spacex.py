import requests
from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.spacex.com/launches/"

# Use Requests
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)
# req = data.text

# Use Selenium
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')

cards = soup.find_all('div', { 'class': ['item'] })

for card in cards:
    date = card.select_one('.date').text
    title = card.select_one('.label').text
    print(f'{date} | {title}')