from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

links = pd.read_csv('decath.csv')
dict = {}
dict = {'names':[],'price':[],'links':[]}
for char in links['links']:
    source = requests.get(char)
    soup = BeautifulSoup(source.text,'lxml')
    dict['names'].append(soup.find('h1',class_='h1 page-title').text)
    dict['price'].append(soup.find('span',itemprop = 'price').text)
    dict['links'].append(char)

print(dict)
csv_file = open('decath2.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['names','price','links'])

for i in range(25):
    csv_writer.writerow([dict['names'][i],dict['price'][i],dict['links'][i]])
csv_file.close()