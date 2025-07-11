def solve():
    """Index: 2958.
    Returns: the number of non-white homes that do not have a fireplace.
    """
    # L1
    total_homes = 400 # The town of Belize has 400 homes
    white_homes_divisor = 4 # One fourth of the town's homes are white
    white_homes = total_homes / white_homes_divisor

    # L2
    non_white_homes = total_homes - white_homes

    # L3
    fireplace_homes_divisor = 5 # One fifth of the non-white homes have a fireplace
    non_white_homes_with_fireplace = non_white_homes / fireplace_homes_divisor

    # L4
    non_white_homes_without_fireplace = non_white_homes - non_white_homes_with_fireplace

    # FA
    answer = non_white_homes_without_fireplace
    return answer