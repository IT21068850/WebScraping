# Car Data Scraper

This project is a web scraping application that collects car listings from the [Ikman.lk](https://ikman.lk) website. It uses Python, BeautifulSoup, and Requests to extract car details like names and prices, and stores the data in a CSV file for further analysis.

## Technologies Used
- **Python**: Programming language used for the project.
- **BeautifulSoup**: Python library used to scrape and parse HTML content.
- **Requests**: Python library used to send HTTP requests.
- **Pandas**: Python library used for creating dataframes and handling data.
- **lxml**: Library used for parsing HTML content.

## Features
- Scrapes car listings from the Ikman.lk website (Sri Lanka's largest online marketplace).
- Collects information such as car name, price, and product link.
- Stores the scraped data in a CSV file (`car_data.csv`) for easy access and analysis.
- Handles pagination to scrape multiple pages of listings.

## Requirements
- Python 3.x
- BeautifulSoup4
- Requests
- Pandas
- lxml

You can install the required packages using pip:

```bash
pip install beautifulsoup4 requests pandas lxml
