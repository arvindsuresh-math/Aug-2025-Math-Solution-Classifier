def solve():
    """Index: 3583.
    Returns: the number of gallons of seed Carson uses.
    """
    # L3
    seed_multiplier = 3 # Each square meter needs three times as much seed as fertilizer
    total_gallons = 60 # 60 gallons of seed and fertilizer combined
    combined_fertilizer_coefficient = seed_multiplier + 1

    # L4
    fertilizer_gallons = total_gallons / combined_fertilizer_coefficient

    # L5
    seed_gallons = seed_multiplier * fertilizer_gallons

    # FA
    answer = seed_gallons
    return answer