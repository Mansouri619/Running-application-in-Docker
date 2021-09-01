# By Zahra Mansouri
# importing modules
import requests
from bs4 import BeautifulSoup
import texttable as tt

# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = iter(soup.find_all('td'))

while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text

        data.append((
            country,
            confirmed,
            deaths,
            continent
        ))

    except StopIteration:
        break

table = tt.Texttable()
table.add_rows([(' Country ', ' Number of cases ', ' Deaths ', ' Continent ')] + data)
table.set_cols_align(["c", "c", "c", "c"])
print(table.draw())
