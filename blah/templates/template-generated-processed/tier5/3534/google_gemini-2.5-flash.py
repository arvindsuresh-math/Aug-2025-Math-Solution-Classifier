def solve():
    """Index: 3534.
    Returns: the number of quarters John has.
    """
    # L2
    fewer_nickels_than_quarters = 6 # 6 fewer nickels than quarters

    # L3
    more_dimes_than_quarters = 3 # three more dimes than quarters

    # L4
    total_coins = 63 # 63 coins

    # L5
    coefficient_x_combined = 1 + 1 + 1 # WK
    constant_combined = -fewer_nickels_than_quarters + more_dimes_than_quarters # WK
    constant_combined_abs = abs(constant_combined) # WK

    # L6
    total_after_constant_move = total_coins - constant_combined

    # L7
    quarters = total_after_constant_move / coefficient_x_combined

    # FA
    answer = quarters
    return answer