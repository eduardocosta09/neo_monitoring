import requests
from datetime import date

class NEOCollector:
    BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"
    def __init__(self, api_key):
        self.api_key = api_key
    def fetch_neos(self):
        today = date.today().isoformat()
        response = requests.get(self.BASE_URL, params={"start_date": today, "end_date": today, "api_key": self.api_key}, timeout=10)
        data = response.json()
        neos = []
        for items in data.get("near_earth_objects", {}).values():
            for item in items:
                diameter = item["estimated_diameter"]["kilometers"]
                approach = item["close_approach_data"][0]
                neos.append({
                    "neo_id": item["id"],
                    "name": item["name"],
                    "diameter_km": (diameter["estimated_diameter_min"] + diameter["estimated_diameter_max"]) / 2,
                    "miss_distance_km": float(approach["miss_distance"]["kilometers"]),
                    "velocity_kmh": float(approach["relative_velocity"]["kilometers_per_hour"]),
                    "approach_date": date.fromisoformat(approach["close_approach_date"])
                })
        return neos
