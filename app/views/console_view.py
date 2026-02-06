def display_neos(neos, limit=10):
    print("\nNEOs processados (preview):\n")

    header = (
        "ID", "Nome", "Diam(km)", "Dist(km)",
        "Vel(km/h)", "Data", "Risco"
    )

    print("{:<10} {:<15} {:<10} {:<12} {:<14} {:<12} {:<8}".format(*header))
    print("-" * 85)

    for neo in neos[:limit]:
        print(
            "{:<10} {:<15} {:<10.2f} {:<12.0f} {:<14.0f} {:<12} {:<8}".format(
                neo.id,
                neo.name[:14],
                neo.diameter_km,
                neo.miss_distance_km,
                neo.velocity_kmh,
                neo.approach_date,
                neo.risk_level
            )
        )
