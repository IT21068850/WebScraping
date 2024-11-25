import requests
from bs4 import BeautifulSoup

baseurl  = 'https://ikman.lk'

headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}


r = requests.get('https://ikman.lk/en/ads/sri-lanka/cars')
soup = BeautifulSoup(r.content,'lxml')

productList = soup.findAll('li', class_ = 'normal--2QYVk gtm-normal-ad')

#print(productList)

productLinks =[]

for items in productList:
    for link in items.findAll('a', href = True):
        # print(link['href'])
        productLinks.append(baseurl + link['href'])



print(len(productLinks))
