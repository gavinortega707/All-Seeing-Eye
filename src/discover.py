import requests
from bs4 import BeautifulSoup

url = "https://www.bottomofthehill.com/calendar.html"

print("Downloading calendar...")

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10,
)

soup = BeautifulSoup(response.text, "html.parser")

print("Page title:")
print(soup.title.text)