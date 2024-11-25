import requests
from bs4 import BeautifulSoup
#BeautifulSoup is a Python library that makes it easy to parse and navigate through HTML or XML

baseurl  = 'https://ikman.lk'

#helps avoid being blocked by the website.
headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    #defines a "user-agent" to mimic a browser request
}

#list to store the links of  individual car ad
productLinks =[]

#for first 5 pages
for x in range (1,5):
    #Sends a GET request to the URL
    r = requests.get(f'https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page={x}')
    
    #Converts the response into a BeautifulSoup object (soup) to make it easier to analyze and extract the HTML content
    soup = BeautifulSoup(r.content,'lxml')

    #This looks for <li> tags with specific classes 
    productList = soup.findAll('li', class_ = 'normal--2QYVk gtm-normal-ad')

    #print(productList)


    for items in productList:
        #it looks for <a> tags with href attributes (these tags contain links).
        for link in items.findAll('a', href = True):
            # print(link['href'])
            #It adds the full URL
            productLinks.append(baseurl + link['href'])



#print(len(productLinks))
