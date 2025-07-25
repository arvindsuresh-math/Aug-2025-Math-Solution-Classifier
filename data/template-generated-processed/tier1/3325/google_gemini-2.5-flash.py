def solve():
    """Index: 3325.
    Returns: the total number of spokes inside the garage.
    """
    # L1
    num_bicycles = 4 # 4 bicycles
    wheels_per_bicycle = 2 # WK
    total_wheels = num_bicycles * wheels_per_bicycle

    # L2
    spokes_per_wheel = 10 # 10 spokes
    total_spokes = total_wheels * spokes_per_wheel

    # FA
    answer = total_spokes
    return answer