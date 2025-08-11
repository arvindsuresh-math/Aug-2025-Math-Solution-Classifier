def solve():
    """Index: 882.
    Returns: the total number of spokes on the bicycle.
    """
    # L1
    front_spokes = 20 # 20 spokes on the front wheel
    back_multiplier = 2 # twice as many spokes on the back wheel
    back_spokes = front_spokes * back_multiplier

    # L2
    total_spokes = front_spokes + back_spokes

    # FA
    answer = total_spokes
    return answer