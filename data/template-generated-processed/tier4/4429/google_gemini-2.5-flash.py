def solve():
    """Index: 4429.
    Returns: the number of 2-liter water bottles Ivy should buy.
    """
    # L1
    water_per_day = 2.5 # 2.5 liters of water each day
    num_days = 4 # 4 days consumption
    total_water_consumed = water_per_day * num_days

    # L2
    bottle_capacity = 2 # 2-liter water
    num_bottles = total_water_consumed / bottle_capacity

    # FA
    answer = num_bottles
    return answer