def solve():
    """Index: 7322.
    Returns: the total number of wheels the vehicles had.
    """
    # L1
    num_bicycles = 50 # 50 bicycles
    wheels_per_bicycle = 2 # WK
    total_bicycle_wheels = num_bicycles * wheels_per_bicycle

    # L2
    num_tricycles = 20 # 20 tricycles
    wheels_per_tricycle = 3 # WK
    total_tricycle_wheels = num_tricycles * wheels_per_tricycle

    # L3
    total_wheels = total_bicycle_wheels + total_tricycle_wheels

    # FA
    answer = total_wheels
    return answer