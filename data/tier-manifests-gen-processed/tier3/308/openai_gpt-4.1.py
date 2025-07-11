def solve():
    """Index: 308.
    Returns: the amount of charcoal Jason adds in grams.
    """
    # L1
    water_per_unit = 30 # 30 ml of water
    charcoal_per_unit = 2 # 2 grams of charcoal
    ml_per_gram = water_per_unit / charcoal_per_unit

    # L2
    total_water = 900 # 900 ml of water
    charcoal_used = total_water / ml_per_gram

    # FA
    answer = charcoal_used
    return answer