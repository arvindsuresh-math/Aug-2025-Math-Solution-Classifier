def solve():
    """Index: 2977.
    Returns: the number of additional minutes Tina can jump rope compared to Cindy.
    """
    # L1
    cindy_jump_minutes = 12 # Cindy can jump rope for 12 minutes
    half_divisor = 2 # half as long as Cindy
    betsy_jump_minutes = cindy_jump_minutes / half_divisor

    # L2
    tina_multiplier = 3 # three times as long as Betsy
    tina_jump_minutes = tina_multiplier * betsy_jump_minutes

    # L3
    difference_minutes = tina_jump_minutes - cindy_jump_minutes

    # FA
    answer = difference_minutes
    return answer