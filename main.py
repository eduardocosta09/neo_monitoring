import sqlite3
from app.collectors.neo_collector import NEOCollector
from app.repositories.neo_repository import NEORepository
from app.services.neo_service import NEOService
from app.reports.csv_reports import generate_csv_report
from app.views.console_view import display_neos


def create_database_connection():
    conn = sqlite3.connect("neo_database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS neo_objects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            neo_id TEXT UNIQUE,
            name TEXT,
            diameter_km REAL,
            miss_distance_km REAL,
            velocity_kmh REAL,
            approach_date TEXT,
            risk_level TEXT
        )
    """)
    conn.commit()
    return conn


def main():
    conn = create_database_connection()

    collector = NEOCollector(api_key="DEMO_KEY")
    repository = NEORepository(conn)
    service = NEOService(collector, repository)

    neos = service.update_neos()

    display_neos(neos)
    generate_csv_report(neos)

    print(f"\nTotal de objetos processados: {len(neos)}")


if __name__ == "__main__":
    main()
