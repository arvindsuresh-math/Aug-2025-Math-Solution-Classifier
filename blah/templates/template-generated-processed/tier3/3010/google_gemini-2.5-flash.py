def solve():
    """Index: 3010.
    Returns: the total number of laundry loads Jon has to do.
    """
    # L1
    total_shirts_to_wash = 20 # wash 20 shirts
    shirts_per_pound = 4 # 4 shirts weigh 1 pound
    shirts_total_weight = total_shirts_to_wash / shirts_per_pound

    # L2
    total_pants_to_wash = 20 # and 20 pants
    pants_per_pound = 2 # 2 pairs of pants weigh 1 pound
    pants_total_weight = total_pants_to_wash / pants_per_pound

    # L3
    total_laundry_weight = pants_total_weight + shirts_total_weight

    # L4
    machine_capacity_pounds = 5 # can do 5 pounds of laundry at a time
    total_loads = total_laundry_weight / machine_capacity_pounds

    # FA
    answer = total_loads
    return answer