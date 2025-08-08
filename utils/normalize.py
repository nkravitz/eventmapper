from dateutil.parser import parse

def normalize_events(events):
    for e in events:
        # Normalize start_time
        if isinstance(e.get("start_time"), str):
            try:
                e["start_time"] = parse(e["start_time"])
            except Exception:
                pass
        # Normalize category
        if "category" in e and isinstance(e["category"], str):
            e["category"] = [c.strip().lower() for c in e["category"].split(",")]
    return events