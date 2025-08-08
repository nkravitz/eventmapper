from scrapers import eventbrite, dcist, gatherdc
from utils.normalize import normalize_events

def run():
    events = []
    events += eventbrite.scrape()
    events += dcist.scrape()
    events += gatherdc.scrape()

    events = normalize_events(events)

    for e in events:
        print(f"{e['start_time']}: {e['title']} @ {e['location']}")

if __name__ == "__main__":
    run()