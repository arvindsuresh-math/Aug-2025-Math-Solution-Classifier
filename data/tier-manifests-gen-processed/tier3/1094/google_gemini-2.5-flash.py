def solve():
    """Index: 1094.
    Returns: the percentage of koolaid powder in the liquid.
    """
    # L1
    initial_water_tbs = 16 # 16 tablespoons of water
    evaporated_water_tbs = 4 # 4 tablespoons of water to evaporate
    water_after_evaporation = initial_water_tbs - evaporated_water_tbs

    # L2
    quadruple_factor = 4 # quadruples the amount of water
    water_after_refill = water_after_evaporation * quadruple_factor

    # L3
    koolaid_powder_tbs = 2 # 2 tablespoons of koolaid power
    total_liquid_volume = water_after_refill + koolaid_powder_tbs

    # L4
    percentage_multiplier = 100 # WK
    koolaid_percentage = (koolaid_powder_tbs / total_liquid_volume) * percentage_multiplier

    # FA
    answer = koolaid_percentage
    return answer