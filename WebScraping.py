import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Base URL for the website
baseurl = 'https://ikman.lk'

# User-Agent header to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# Set to store unique links for car ads
# Set does not allow duplicate elements 
productLinks = set()

# Scrape the first 5 pages
for x in range(1, 2):
    # Sends a GET request to the URL
    r = requests.get(f'{baseurl}/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page={x}', headers=headers)
    
    # Converts the response into a BeautifulSoup object to analyze HTML content
    soup = BeautifulSoup(r.content, 'lxml')

    # Find all car ad items
    productList = soup.findAll('li', class_='normal--2QYVk gtm-normal-ad')

    # Loop through items and extract unique links
    for items in productList:
        for link in items.findAll('a', href=True):
            full_url = baseurl + link['href']
            productLinks.add(full_url)  # Add to the set

# Print all unique product links
print(f"Total unique links: {len(productLinks)}")
print(productLinks)

# Extract details from each unique product link
carList = []
for link in productLinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    # Extract car name and price
    name = soup.find('h1', class_='title--3s1R8').text.strip() if soup.find('h1', class_='title--3s1R8') else 'N/A'
    datePosted = soup.find('div', class_ = 'subtitle-wrapper--1M5Mv').text.strip() if soup.find('div', class_ = 'subtitle-wrapper--1M5Mv') else 'N/A'
    price = soup.find('div', class_='amount--3NTpl').text.strip() if soup.find('div', class_='amount--3NTpl') else 'N/A'

    # Extract only the date and month from the 'datePosted' text using regular expressions
    date_match = re.search(r'(\d{1,2} [A-Za-z]+)', datePosted)
    if date_match:
        datePosted = date_match.group(1)
    else:
        datePosted = 'N/A'

    # Store car details in a dictionary
    car = {
        'Name': name,
        'Price': price,
        'Date Posted': datePosted
    }
    print(car)
    carList.append(car)



#Displaying CarList Dataframe
df = pd.DataFrame(carList)
print(df.head(15))
#Export Dataframe to csv
df.to_csv('DataSet/car_data.csv', index=False)

