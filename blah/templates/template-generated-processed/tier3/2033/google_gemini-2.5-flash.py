def solve():
    """Index: 2033.
    Returns: the number of additional cars one level can fit.
    """
    # L1
    total_capacity = 425 # room for 425 cars
    num_levels = 5 # 5 levels
    capacity_per_level = total_capacity / num_levels

    # L2
    parked_cars = 23 # already 23 parked cars on that level
    remaining_capacity = capacity_per_level - parked_cars

    # FA
    answer = remaining_capacity
    return answer