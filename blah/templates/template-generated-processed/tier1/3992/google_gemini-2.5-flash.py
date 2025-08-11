def solve():
    """Index: 3992.
    Returns: the total pounds of lobster the three harbors are holding.
    """
    # L1
    other_harbor_pounds = 80 # 80 pounds of lobster each
    combined_other_harbors = other_harbor_pounds + other_harbor_pounds

    # L2
    hooper_bay_multiplier = 2 # twice as many pounds of lobster
    hooper_bay_pounds = hooper_bay_multiplier * combined_other_harbors

    # L3
    total_pounds = hooper_bay_pounds + combined_other_harbors

    # FA
    answer = total_pounds
    return answer