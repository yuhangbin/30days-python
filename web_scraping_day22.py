import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    facts = {}

    facts['body'] = soup.get_text()
    return facts

print(scrape('http://www.bu.edu/president/boston-university-facts-stats/'))


def extract_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    print(tables)

extract_table('https://archive.ics.uci.edu/ml/datasets.php')
import json
def scrape_and_store(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    presidents = []
    for row in table.find_all('tr')[1:]:  # Skip the header row
        columns = row.find_all('td')
        if len(columns) >= 6:  # Ensure we have enough columns
            president = {
                'number': columns[0].text.strip(),
                'name': columns[1].text.strip(),
                'term': columns[2].text.strip(),
                'party': columns[3].text.strip(),
                'election': columns[4].text.strip(),
                'vice_president': columns[5].text.strip()
            }
            presidents.append(president)
    with open('presidents.json', 'w') as f:
        json.dump(presidents, f, indent=2)
    return presidents

scrape_and_store('https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States')

