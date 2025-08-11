def solve():
    """Index: 4716.
    Returns: the total number of wheels.
    """
    # L1
    bicycle_wheels_per_bicycle = 2 # Each bicycle has 2 wheels
    num_bicycles = 3 # 3 bicycles
    total_bicycle_wheels = bicycle_wheels_per_bicycle * num_bicycles

    # L2
    tricycle_wheels_per_tricycle = 3 # each tricycle has 3 wheels
    num_tricycles = 4 # 4 tricycles
    total_tricycle_wheels = tricycle_wheels_per_tricycle * num_tricycles

    # L3
    unicycle_wheels_per_unicycle = 1 # each unicycle has 1 wheel
    num_unicycles = 7 # 7 unicycles
    total_unicycle_wheels = unicycle_wheels_per_unicycle * num_unicycles

    # L4
    total_wheels = total_bicycle_wheels + total_tricycle_wheels + total_unicycle_wheels

    # FA
    answer = total_wheels
    return answer