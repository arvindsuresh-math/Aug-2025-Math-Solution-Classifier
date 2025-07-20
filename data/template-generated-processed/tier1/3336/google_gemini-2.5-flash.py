def solve():
    """Index: 3336.
    Returns: the total number of wheels Dimitri saw at the park.
    """
    # L1
    bicycle_wheels_per_bike = 2 # WK
    num_adults_riding_bicycles = 6 # 6 adults were riding bicycles
    bicycle_wheels_total = bicycle_wheels_per_bike * num_adults_riding_bicycles

    # L2
    tricycle_wheels_per_trike = 3 # WK
    num_children_riding_tricycles = 15 # 15 children were riding tricycles
    tricycle_wheels_total = num_children_riding_tricycles * tricycle_wheels_per_trike

    # L3
    total_wheels = bicycle_wheels_total + tricycle_wheels_total

    # FA
    answer = total_wheels
    return answer