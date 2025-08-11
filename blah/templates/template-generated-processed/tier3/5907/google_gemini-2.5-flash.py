def solve():
    """Index: 5907.
    Returns: the percentage chance Renee will have an allergic reaction.
    """
    # L1
    jenny_pb_cookies = 40 # 40 peanut butter cookies
    marcus_pb_cookies = 30 # 30 peanut butter cookies
    total_pb_cookies = jenny_pb_cookies + marcus_pb_cookies

    # L2
    jenny_cc_cookies = 50 # 50 chocolate chip cookies
    marcus_lemon_cookies = 20 # 20 lemon cookies
    total_cookies = total_pb_cookies + jenny_cc_cookies + marcus_lemon_cookies

    # L3
    percentage_multiplier = 100 # 100%
    allergic_reaction_percentage = total_pb_cookies / total_cookies * percentage_multiplier

    # FA
    answer = allergic_reaction_percentage
    return answer