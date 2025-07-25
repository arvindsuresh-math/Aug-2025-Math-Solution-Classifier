def solve():
    """Index: 3756.
    Returns: the number of Schnauzers.
    """
    # L1
    multiplier_three = 3 # three times
    num_doberman_puppies = 20 # number of Doberman puppies is 20
    three_times_doberman = multiplier_three * num_doberman_puppies

    # L2
    five_less = 5 # Five less
    five_less_three_times = three_times_doberman - five_less

    # L7
    # The equation is: five_less_three_times + (s - num_doberman_puppies) = total_sum
    # 55 + s - 20 = 90
    total_sum = 90 # equal to 90
    constant_term_simplified = five_less_three_times - num_doberman_puppies

    # L8
    num_schnauzers = total_sum - constant_term_simplified

    # FA
    answer = num_schnauzers
    return answer