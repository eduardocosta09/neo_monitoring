def classify_risk(diameter_km, miss_distance_km):
    if diameter_km >= 1.0 and miss_distance_km <= 5_000_000:
        return "ALTO"
    if 0.3 <= diameter_km < 1.0:
        return "MODERADO"
    if 5_000_000 < miss_distance_km <= 20_000_000:
        return "MODERADO"
    return "BAIXO"
