def solve():
    """Index: 102.
    Returns: the total amount of oil Ellie needs to fix the bike.
    """
    # L1
    num_wheels = 2 # 2 wheels
    oil_per_wheel = 10 # 10ml of oil to fix each wheel
    oil_for_wheels = num_wheels * oil_per_wheel

    # L2
    oil_for_rest = 5 # another 5ml of oil to fix the rest of the bike
    total_oil = oil_for_wheels + oil_for_rest

    # FA
    answer = total_oil
    return answer