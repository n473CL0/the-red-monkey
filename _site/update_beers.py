import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Map beer types to hex codes
type_color_map = {
    "stout": "#0A0A0A",
    "porter": "#2B1B17",
    "dark": "#2B1B17",
    "brown": "#5C4033",
    "ruby": "#9B111E",
    "red": "#8B0000",
    "bitter": "#B87333",
    "ipa": "#EAA221",
    "pale ale": "#F3E5AB",
    "blonde": "#F3D55B",
    "lager": "#F3D55B",
    "pils": "#F3D55B",
    "kellerbier": "#F3D55B",
    "cider": "#E8D882"
}

def get_color_from_type(details_text):
    text_lower = details_text.lower()
    for beer_type, hex_code in type_color_map.items():
        if beer_type in text_lower:
            return hex_code
    return None

url = "https://www.realalefinder.com/beerboard/?the-red-monkey-bristol"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

beers = []
sections = ['beernow', 'kegnow', 'cidersnow']

for section_class in sections:
    section = soup.find('div', class_=section_class)
    if not section:
        continue
        
    for item in section.find_all('div', class_='beer-item'):
        h2_tags = item.find_all('h2')
        
        if len(h2_tags) >= 3:
            name = h2_tags[0].text.strip()
            brewery = h2_tags[1].text.strip()
            details = h2_tags[2].text.strip()
        else:
            continue
            
        notes_tag = item.find('p', class_='tasting-notes')
        notes = notes_tag.text.strip() if notes_tag else ""
        
        hex_color = get_color_from_type(details)

        # Extract the image URL
        img_tag = item.find('img')
        if img_tag and img_tag.has_attr('src'):
            raw_img_url = img_tag['src']
            # urljoin ensures that even if the raw link is relative, it becomes a fully working URL
            image_url = urljoin(url, raw_img_url) 
        else:
            image_url = None

        beers.append({
            'beer_name': name,
            'brewery': brewery,
            'details': details,
            'notes': notes,
            'color': hex_color,
            'image': image_url
        })

with open('_data/beers.json', 'w') as f:
    json.dump(beers, f, indent=2)