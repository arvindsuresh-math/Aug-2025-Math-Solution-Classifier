def solve():
    """Index: 6234.
    Returns: the number of hops the second frog took to cross the road.
    """
    # L2
    second_frog_multiplier = 2 # twice as many as the third
    second_frog_coefficient = second_frog_multiplier

    # L3
    first_frog_multiplier = 4 # 4 times as many hops as the second
    first_frog_coefficient = first_frog_multiplier * second_frog_coefficient

    # L4
    total_hops = 99 # total of 99 hops
    third_frog_coefficient = 1 # WK (implied coefficient for 'x')
    sum_of_coefficients = third_frog_coefficient + second_frog_coefficient + first_frog_coefficient

    # L6
    third_frog_hops = total_hops / sum_of_coefficients

    # L7
    second_frog_actual_hops = second_frog_multiplier * third_frog_hops

    # FA
    answer = second_frog_actual_hops
    return answer