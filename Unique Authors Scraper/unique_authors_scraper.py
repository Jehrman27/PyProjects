"""
Author Scraper

This program scrapes the quotes on https://quotes.toscrape.com
and creates a list of unique author names.
"""
import requests
import bs4


BASE_URL = 'https://quotes.toscrape.com/page/{}/'
PAGE_NO = 1
authors = set()

while True:
    # Request page number PAGE_NO and make soup
    res = requests.get(BASE_URL.format(PAGE_NO))
    soup = bs4.BeautifulSoup(res.text,'lxml')

    # Find all authors on the page
    page_auths = soup.select('.author')

    if len(page_auths) == 0:
        # If no quotes found, reached end of valid pages.
        break

    # Add the author text into the authors set
    for a in page_auths:
        authors.add(a.text)

    # Increment page number
    PAGE_NO += 1

# Print each author on a separate line.
print(*authors, sep='\n')
