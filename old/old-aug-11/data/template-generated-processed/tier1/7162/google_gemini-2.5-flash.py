def solve():
    """Index: 7162.
    Returns: the number of feathers the chicken had afterward.
    """
    # L1
    cars_dodged = 23 # 23 speeding cars
    multiplier_feathers = 2 # twice as many feathers
    feathers_lost_second_crossing = cars_dodged * multiplier_feathers

    # L2
    initial_feathers = 5263 # 5263 feathers before its thrill-seeking road crossings
    feathers_after = initial_feathers - feathers_lost_second_crossing

    # FA
    answer = feathers_after
    return answer