from app.models.neo import NEO
from app.processors.risk_analyzer import classify_risk

class NEOService:
    def __init__(self, collector, repository):
        self.collector = collector
        self.repository = repository
    def update_neos(self):
        processed = []
        items = self.collector.fetch_neos()
        print(f"NEOs recebidos do collector: {len(items)}")
        for item in self.collector.fetch_neos():
            risk = classify_risk(item["diameter_km"], item["miss_distance_km"])
            neo = NEO(item["neo_id"], item["name"], item["diameter_km"], item["miss_distance_km"], item["velocity_kmh"], item["approach_date"], risk)
            self.repository.save(neo)
            processed.append(neo)
        return processed
