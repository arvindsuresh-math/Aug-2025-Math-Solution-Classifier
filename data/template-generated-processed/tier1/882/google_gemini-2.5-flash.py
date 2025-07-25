def solve():
    """Index: 882.
    Returns: the total number of spokes the bicycle has.
    """
    # L1
    front_wheel_spokes = 20 # 20 spokes on the front wheel
    multiplier_for_back_wheel = 2 # twice as many spokes
    back_wheel_spokes = front_wheel_spokes * multiplier_for_back_wheel

    # L2
    total_spokes = front_wheel_spokes + back_wheel_spokes

    # FA
    answer = total_spokes
    return answer