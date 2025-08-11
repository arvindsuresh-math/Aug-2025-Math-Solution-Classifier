def solve():
    """Index: 5049.
    Returns: the number Armand's dad is thinking of.
    """
    # L1
    twice_factor = 2 # WK
    original_number_dad_thought_of = 51 # twice 51
    twice_original_number = twice_factor * original_number_dad_thought_of

    # L2
    three_less = 3 # three less than
    value_three_less_than_twice = twice_original_number - three_less

    # L3
    multiplication_factor = 3 # when multiplied by 3
    the_number = value_three_less_than_twice / multiplication_factor

    # FA
    answer = the_number
    return answer