def solve():
    """Index: 5506.
    Returns: the total liters of water needed to fill both tanks.
    """
    # L1
    second_tank_filled_liters = 450 # second tank is 450 liters filled
    second_tank_filled_percentage = 45 # second tank is only 45% filled
    liters_per_percent = second_tank_filled_liters / second_tank_filled_percentage

    # L2
    total_percentage = 100 # WK
    tank_capacity = liters_per_percent * total_percentage

    # L3
    first_tank_filled_liters = 300 # first tank is 300 liters filled
    first_tank_needed = tank_capacity - first_tank_filled_liters

    # L4
    second_tank_needed = tank_capacity - second_tank_filled_liters

    # L5
    total_liters_needed = first_tank_needed + second_tank_needed

    # FA
    answer = total_liters_needed
    return answer