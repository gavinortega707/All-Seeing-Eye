import requests
from bs4 import BeautifulSoup

url = "https://www.bottomofthehill.com/calendar.html"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
)

soup = BeautifulSoup(response.text, "html.parser")

bands = soup.find_all(class_="band")

print(f"Found {len(bands)} bands:\n")

for band in bands[:20]:
    print("-", band.get_text(strip=True))