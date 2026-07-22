import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://www.bottomofthehill.com/calendar.html"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10,
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

event_cells = soup.find_all("td")

events = []

for cell in event_cells:
    bands = cell.find_all(class_="band")

    if not bands:
        continue

    date_parts = cell.find_all(class_="date")
    time_parts = cell.find_all(class_="time")
    cover_parts = cell.find_all(class_="cover")
    genres = cell.find_all(class_="genre")

    date = "".join(
        part.get_text(" ", strip=True)
        for part in date_parts
        if part.get_text(" ", strip=True)
   )

    date = " ".join(date.split())

    time = " ".join(
        part.get_text(" ", strip=True)
        for part in time_parts
        if part.get_text(" ", strip=True)
    )

    time = time.replace(" :", ":")

    price = " ".join(
        part.get_text(" ", strip=True)
        for part in cover_parts
        if part.get_text(" ", strip=True)
    )

    price = " ".join(price.split())

    band_names = [
        band.get_text(" ", strip=True)
        for band in bands
    ]

    genre_names = [
        genre.get_text(" ", strip=True)
        for genre in genres
    ]

    event = {
        "venue": "Bottom of the Hill",
        "date": date,
        "time": time,
        "price": price,
        "bands": band_names,
        "genres": genre_names,
    }

    events.append(event)

print(f"Found {len(events)} events.\n")

for event in events[:3]:
    pprint(event, sort_dicts=False)
    print("-" * 50)