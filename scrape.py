# scrape.py
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = 'https://quotes.toscrape.com/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = []
for quote in soup.select('.quote'):
    quotes.append({
        'text': quote.select_one('.text').get_text(),
        'author': quote.select_one('.author').get_text()
    })

filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(quotes, f, indent=2, ensure_ascii=False)

print(f"Saved {len(quotes)} quotes to {filename}")
