def solve():
    """Index: 3361.
    Returns: the number of years until Agnes is twice as old as Jane.
    """
    # L3
    agnes_current_age = 25 # Agnes is 25 years old
    jane_current_age = 6 # Jane is 6 years old
    twice_multiplier = 2 # twice as old
    expanded_jane_age_term = twice_multiplier * jane_current_age
    rhs_constant_after_expansion = expanded_jane_age_term - agnes_current_age

    # L4
    simplified_rhs_value = rhs_constant_after_expansion

    # L5
    x_value = -1 * simplified_rhs_value

    # FA
    answer = x_value
    return answer