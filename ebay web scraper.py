from bs4 import BeautifulSoup
import requests
import csv

def get_page(url):
    source = requests.get(url)
    
    if source.ok:
        soup = BeautifulSoup(source.text,'lxml')
    
    else:
        print('Server responded:', source.status_code)
    
    return soup

def get_detail_data(soup):
    # item
    # price
    # items sold
    try:
        title = soup.find('h1',id='itemTitle').text.split('  ')[1].replace('\xa0','')
    except:
        title = ''
    
    try:
        price = soup.find("span", id = 'convbinPrice').text
    except:
        price = ''
    
    
    try:
        sold = soup.find('span',class_='vi-qtyS').find('a').text
    except:
        sold = 'None sold'
    
    data = {'Name':title,'Price':price,'Total sold':sold}
    
    return data

def get_index_data(soup):
    try:
        links = soup.find_all('a',class_='vip')
    except:
        links = []
    
    urls = [x.get('href') for x in links]
    
    return urls

def main():
    
    csv_file = open('output.csv','w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['name','price','link'])
    
    for pg in range(1,4):
        url = 'https://www.ebay.com.sg/sch/i.html?_nkw=sudio+wireless&_pgn=' + str(pg)
    
        prods = get_index_data(get_page(url))
        
        for link in prods:
            data = get_detail_data(get_page(link))
            data['link'] = link
            csv_writer.writerow([data['Name'],data['Price'],data['link']])
            print(data)
            print()
    
    csv_file.close()

if __name__ == '__main__':
    output = main()
    