import requests
from bs4 import BeautifulSoup

url = "https://www.bottomofthehill.com/calendar.html"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10,
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

event_cells = soup.find_all("td")

events_found = 0

for cell in event_cells:
    bands = cell.find_all(class_="band")

    # Skip table cells that are not concert listings.
    if not bands:
        continue

    date_parts = cell.find_all(class_="date")
    time_parts = cell.find_all(class_="time")
    cover_parts = cell.find_all(class_="cover")
    genres = cell.find_all(class_="genre")

    date = " ".join(
        part.get_text(" ", strip=True)
        for part in date_parts
        if part.get_text(" ", strip=True)
    )

    time = " ".join(
        part.get_text(" ", strip=True)
        for part in time_parts
        if part.get_text(" ", strip=True)
    )

    price = " ".join(
        part.get_text(" ", strip=True)
        for part in cover_parts
        if part.get_text(" ", strip=True)
    )

    band_names = [
        band.get_text(" ", strip=True)
        for band in bands
    ]

    genre_names = [
        genre.get_text(" ", strip=True)
        for genre in genres
    ]

    events_found += 1

    print(f"Event {events_found}")
    print("Date:", date)
    print("Time:", time)
    print("Price:", price)
    print("Bands:", ", ".join(band_names))
    print("Genres:", ", ".join(genre_names))
    print("-" * 50)

print(f"\nFound {events_found} events.")