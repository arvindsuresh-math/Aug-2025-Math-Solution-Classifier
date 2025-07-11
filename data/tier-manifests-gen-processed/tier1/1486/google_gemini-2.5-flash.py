def solve():
    """Index: 1486.
    Returns: the total number of haircuts Tammy has gotten.
    """
    # L1
    haircuts_per_free_one = 14 # For every 14 haircuts
    free_haircuts_received = 5 # gotten 5 free haircuts already
    haircuts_for_free_ones = haircuts_per_free_one * free_haircuts_received

    # L2
    haircuts_away_from_next_free = 5 # 5 haircuts away from another free one
    haircuts_towards_next_free = haircuts_per_free_one - haircuts_away_from_next_free

    # L3
    total_haircuts = haircuts_for_free_ones + haircuts_towards_next_free

    # FA
    answer = total_haircuts
    return answer