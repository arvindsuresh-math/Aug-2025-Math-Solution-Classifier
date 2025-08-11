def solve():
    """Index: 4900.
    Returns: Allyson's age.
    """
    # L1
    hiram_age = 40 # Hiram is 40 years old
    add_value_1 = 12 # add 12
    hiram_age_plus_12 = hiram_age + add_value_1

    # L2
    add_value_2 = 4 # 4 less than twice Allyson's age
    twice_allyson_age = hiram_age_plus_12 + add_value_2

    # L3
    divisor_for_half = 2 # twice Allyson's age
    allyson_age = twice_allyson_age / divisor_for_half

    # FA
    answer = allyson_age
    return answer