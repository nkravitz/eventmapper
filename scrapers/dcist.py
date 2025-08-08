from datetime import datetime

def scrape():
    print("Scraping DCist...")
    return [{
        "title": "DCist Mock Concert",
        "start_time": "2025-08-16T20:00:00",
        "location": "9:30 Club, Washington, DC",
        "latitude": None,
        "longitude": None,
        "category": "Music",
        "description": "Fake concert listing from DCist.",
        "link": "https://dcist.com/fake-event",
        "source": "dcist"
    }]