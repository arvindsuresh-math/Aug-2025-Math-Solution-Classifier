def solve():
    """Index: 2555.
    Returns: the weight of the moon in tons.
    """
    # L1
    total_percent = 100 # WK
    iron_percent = 50 # 50% iron
    carbon_percent = 20 # 20% carbon
    other_percent = total_percent - iron_percent - carbon_percent

    # L2
    mars_other_tons = 150 # Mars is 150 tons of other elements
    other_percent_decimal = 0.3 # 30% as decimal
    mars_weight = mars_other_tons / other_percent_decimal

    # L3
    mars_to_moon_ratio = 2 # Mars weighs twice as much as the moon
    moon_weight = mars_weight / mars_to_moon_ratio

    # FA
    answer = moon_weight
    return answer