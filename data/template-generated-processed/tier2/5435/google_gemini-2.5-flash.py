def solve():
    """Index: 5435.
    Returns: the amount of protein powder Matt needs to eat per week.
    """
    # L1
    body_weight_kg = 80 # weighs 80 kg
    protein_per_kg = 2 # 2 grams of protein per kilogram of body weight
    daily_protein_needed = body_weight_kg * protein_per_kg

    # L2
    protein_powder_protein_percentage = 0.8 # 80% protein
    daily_protein_powder_needed = daily_protein_needed / protein_powder_protein_percentage

    # L3
    days_per_week = 7 # WK
    weekly_protein_powder_needed = daily_protein_powder_needed * days_per_week

    # FA
    answer = weekly_protein_powder_needed
    return answer