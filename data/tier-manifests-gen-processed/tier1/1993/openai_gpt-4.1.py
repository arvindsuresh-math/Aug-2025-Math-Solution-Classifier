def solve():
    """Index: 1993.
    Returns: the total number of coughs by Georgia and Robert after 20 minutes.
    """
    # L1
    georgia_coughs_per_min = 5 # Georgia coughs 5 times a minute
    robert_multiplier = 2 # Robert coughs twice as much as her
    robert_coughs_per_min = robert_multiplier * georgia_coughs_per_min

    # L2
    total_coughs_per_min = georgia_coughs_per_min + robert_coughs_per_min

    # L3
    minutes = 20 # After 20 minutes
    total_coughs = total_coughs_per_min * minutes

    # FA
    answer = total_coughs
    return answer