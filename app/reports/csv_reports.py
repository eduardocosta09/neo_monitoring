import csv
import os


def generate_csv_report(neos, file_path="reports/neo_daily_report.csv"):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "id",
            "name",
            "diameter_km",
            "miss_distance_km",
            "velocity_kmh",
            "approach_date",
            "risk_level"
        ])

        for neo in neos:
            writer.writerow([
                neo.id,
                neo.name,
                neo.diameter_km,
                neo.miss_distance_km,
                neo.velocity_kmh,
                neo.approach_date,
                neo.risk_level
            ])
