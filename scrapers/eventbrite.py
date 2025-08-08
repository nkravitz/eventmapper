from datetime import datetime

def scrape():
    print("Scraping Eventbrite...")
    return [{
        "title": "Eventbrite Demo Event",
        "start_time": "2025-08-15T18:00:00",
        "location": "1401 Constitution Ave NW, Washington, DC",
        "latitude": None,
        "longitude": None,
        "category": "Tech, Networking",
        "description": "A mock Eventbrite event.",
        "link": "https://eventbrite.com/fake-event",
        "source": "eventbrite"
    }]
