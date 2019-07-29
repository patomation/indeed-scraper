import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', 'Accept-Language': 'en'}

def parse(url):

    print '...Scraping...'

    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, 'html.parser')
