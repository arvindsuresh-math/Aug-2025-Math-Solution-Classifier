def solve():
    """Index: 1052.
    Returns: James's age.
    """
    # L1
    john_age_at_james_23 = 35 # John turned 35
    james_age_at_john_35 = 23 # James turned 23
    age_difference = john_age_at_james_23 - james_age_at_john_35

    # L2
    tim_current_age = 79 # If Tim is 79
    age_offset = 5 # 5 years less than
    value_for_twice_johns_age = tim_current_age - age_offset

    # L3
    divisor_for_johns_age = 2 # twice John's age
    johns_current_age = value_for_twice_johns_age / divisor_for_johns_age

    # L4
    james_current_age = johns_current_age - age_difference

    # FA
    answer = james_current_age
    return answer