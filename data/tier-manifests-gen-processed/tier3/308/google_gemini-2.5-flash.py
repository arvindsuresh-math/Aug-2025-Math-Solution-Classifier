def solve():
    """Index: 308.
    Returns: the amount of charcoal Jason adds.
    """
    # L1
    water_per_charcoal_ratio_ml = 30 # 30 ml of water
    charcoal_per_charcoal_ratio_g = 2 # 2 grams of charcoal
    ml_per_gram_charcoal = water_per_charcoal_ratio_ml / charcoal_per_charcoal_ratio_g

    # L2
    total_water_ml = 900 # 900 ml of water
    total_charcoal_g = total_water_ml / ml_per_gram_charcoal

    # FA
    answer = total_charcoal_g
    return answer