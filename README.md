# EventMapper

**EventMapper** is a social calendar aggregator that scrapes local event listings, unifies them into a standard format, and visualizes them on an interactive map with filtering by date, location, and category.

## 🚀 Goals

- Aggregate multiple public event sources (Eventbrite, university sites, local blogs)
- Normalize and geocode event data
- Visualize events on a map and in tables
- Enable users to find events by time, place, and interest
- Host a frontend app (Streamlit or Flask)

## 🔨 Current Status

| Stage | Description | Status |
|-------|-------------|--------|
| 0     | Project scaffold + README | ✅ Complete |
| 1     | Hardcoded one-event map prototype | ⏳ Next |
| 2     | First working scraper (e.g. Eventbrite) | ☐ |
| 3     | Normalization and filtering | ☐ |
| 4     | Tabular display | ☐ |
| 5     | Web frontend | ☐ |

## 📁 Project Structure

```
eventmapper/
├── main.py
├── config.py
├── scrapers/
├── utils/
├── app/
├── data/
│   ├── raw/
│   ├── processed/
│   └── cache/
├── README.md
├── requirements.txt
└── .gitignore
```

## 🧠 Tech Stack

- Python (requests, BeautifulSoup, pandas, folium, geopy)
- Streamlit or Flask (TBD)
- Git + GitHub for version control
