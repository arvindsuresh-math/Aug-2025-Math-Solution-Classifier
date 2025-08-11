def solve():
    """Index: 1343.
    Returns: the number of pairs of purple shoes in the warehouse.
    """
    # L1
    total_shoes = 1250 # There are 1250 pairs of shoes in the warehouse
    blue_shoes = 540 # 540 pairs that are blue
    remaining_shoes = total_shoes - blue_shoes

    # L2
    divisor_for_green_purple = 2 # The number of green shoes is equal to the number of purple shoes
    purple_shoes = remaining_shoes / divisor_for_green_purple

    # FA
    answer = purple_shoes
    return answer