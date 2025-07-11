def solve():
    """Index: 2555.
    Returns: the weight of the moon in tons.
    """
    # L1
    total_percent = 100 # WK
    iron_percent = 50 # 50% iron
    carbon_percent = 20 # 20% carbon
    other_elements_percent = total_percent - iron_percent - carbon_percent

    # L2
    mars_other_elements_weight = 150 # Mars is 150 tons of other elements
    other_elements_decimal = other_elements_percent / 100
    mars_weight = mars_other_elements_weight / other_elements_decimal

    # L3
    mars_moon_weight_ratio = 2 # Mars weighs twice as much as the moon
    moon_weight = mars_weight / mars_moon_weight_ratio

    # FA
    answer = moon_weight
    return answer