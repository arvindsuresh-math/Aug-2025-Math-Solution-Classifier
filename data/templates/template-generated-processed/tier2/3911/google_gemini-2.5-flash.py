def solve():
    """Index: 3911.
    Returns: the total weight of Bill's improvised weights.
    """
    # L1
    jug_capacity_gallons = 2 # two 2-gallon jugs
    fill_percentage_num = 70 # fills them 70% full
    percent_to_decimal_factor = 0.01 # WK
    volume_one_jug = jug_capacity_gallons * fill_percentage_num * percent_to_decimal_factor

    # L2
    num_jugs = 2 # two 2-gallon jugs
    total_volume = volume_one_jug * num_jugs

    # L3
    sand_density = 5 # sand has a density of 5 pounds/gallon
    total_weight = total_volume * sand_density

    # FA
    answer = total_weight
    return answer