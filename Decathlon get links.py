from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import csv


driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.decathlon.sg/?query=elastic%20resistance%20band'
driver.get(url)
x = []
for i in range(1,26):
    char = '//*[@id="hits"]/div/div/ol/li[' + str(i) + ']/article/div[2]/h3'
    x.append(driver.find_elements_by_xpath(char))
links = []
links = [v[0].find_element_by_tag_name('a').get_attribute('href') for v in x]
driver.close()
csv_file = open('decath.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['links'])

for link in links:
    print(link)
    csv_writer.writerow([link])

csv_file.close()

