import sqlite3
from app.models.neo import NEO

class NEORepository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, neo):
        cursor = self.connection.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO neo_objects
            (neo_id, name, diameter_km, miss_distance_km, velocity_kmh, approach_date, risk_level)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                neo.id,
                neo.name,
                neo.diameter_km,
                neo.miss_distance_km,
                neo.velocity_kmh,
                neo.approach_date.isoformat(),
                neo.risk_level
            )
        )
        self.connection.commit()
