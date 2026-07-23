from pprint import pprint

from src.venues.bottom_of_the_hill import get_events


def main():
    events = get_events()

    print(f"Found {len(events)} events.\n")

    for event in events[:3]:
        pprint(event)
        print("-" * 50)


if __name__ == "__main__":
    main()