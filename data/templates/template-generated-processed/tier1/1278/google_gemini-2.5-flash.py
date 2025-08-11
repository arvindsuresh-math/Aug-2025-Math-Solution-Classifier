def solve():
    """Index: 1278.
    Returns: the total length of the two pieces of yarn in centimeters.
    """
    # L1
    green_yarn_length_cm = 156 # The green piece of yarn is 156 cm long.

    # L2
    red_yarn_multiplier = 3 # three times the length
    red_yarn_addition_cm = 8 # 8 cm more
    red_yarn_length_cm = red_yarn_multiplier * green_yarn_length_cm + red_yarn_addition_cm

    # L3
    total_length_cm = green_yarn_length_cm + red_yarn_length_cm

    # FA
    answer = total_length_cm
    return answer