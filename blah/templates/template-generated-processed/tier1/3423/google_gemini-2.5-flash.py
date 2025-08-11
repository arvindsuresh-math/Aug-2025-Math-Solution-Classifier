def solve():
    """Index: 3423.
    Returns: the number of chickens free ranging.
    """
    # L1
    chickens_in_coop = 14 # 14 chickens in the coop

    # L2
    multiplier_for_run = 2 # twice that many
    chickens_in_run = chickens_in_coop * multiplier_for_run

    # L3
    multiplier_for_free_range = 2 # double the number of chickens
    less_than_double = 4 # 4 less than double
    chickens_free_ranging = chickens_in_run * multiplier_for_free_range - less_than_double

    # FA
    answer = chickens_free_ranging
    return answer