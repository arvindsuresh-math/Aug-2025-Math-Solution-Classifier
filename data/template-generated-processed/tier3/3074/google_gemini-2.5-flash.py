def solve():
    """Index: 3074.
    Returns: the percentage chance Carter will get a green M&M.
    """
    # L1
    initial_green_mms = 20 # 20 green M&Ms
    eaten_green_mms = 12 # eats 12 of the green M&Ms
    final_green_mms = initial_green_mms - eaten_green_mms

    # L2
    initial_red_mms = 20 # 20 red M&Ms
    half_divisor = 2 # eats half the red M&Ms
    final_red_mms = initial_red_mms / half_divisor

    # L3
    added_yellow_mms = 14 # adds 14 yellow M&Ms
    total_mms = final_green_mms + final_red_mms + added_yellow_mms

    # L4
    percentage_multiplier = 100 # multiply by 100 to find the percentage chance
    percentage_green_mms = (final_green_mms / total_mms) * percentage_multiplier

    # FA
    answer = percentage_green_mms
    return answer