import requests
from bs4 import BeautifulSoup
#BeautifulSoup is a Python library that makes it easy to parse and navigate through HTML or XML

baseurl  = 'https://ikman.lk'

#helps avoid being blocked by the website.
headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    #defines a "user-agent" to mimic a browser request
}


#print(len(productLinks))
testLink = 'https://ikman.lk/en/ad/audi-e-tron-q8-50-quattro-2024-for-sale-colombo-4'
r= requests.get(testLink,headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

name = soup.find('h1',class_='title--3s1R8').text.strip()
price = soup.find('div', class_ ='amount--3NTpl').text.strip()
description = soup.find('div',class_='description--1nRbz').text.strip()

Car = {
    'Name': name,
    'Price': price,
    'description': description
}

print(Car)
