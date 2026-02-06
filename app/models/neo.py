class NEO:
    def __init__(
        self,
        neo_id,
        name,
        diameter_km,
        miss_distance_km,
        velocity_kmh,
        approach_date,
        risk_level
    ):
        self.id = neo_id
        self.name = name
        self.diameter_km = diameter_km
        self.miss_distance_km = miss_distance_km
        self.velocity_kmh = velocity_kmh
        self.approach_date = approach_date
        self.risk_level = risk_level
