def solve():
    """Index: 3394.
    Returns: the tons of sand City D received.
    """
    # L1
    city_a_sand = 16.5 # City A received 16 1/2 tons of sand
    city_c_sand = 24.5 # City C received 24 1/2 tons of sand
    total_sand_ac = city_a_sand + city_c_sand

    # L2
    city_b_sand = 26 # City B received 26 tons of sand
    total_sand_abc = total_sand_ac + city_b_sand

    # L3
    total_sand_all_cities = 95 # the total for all four cities was 95 tons
    city_d_sand = total_sand_all_cities - total_sand_abc

    # FA
    answer = city_d_sand
    return answer