def solve():
    """Index: 1486.
    Returns: the total number of haircuts Tammy has gotten.
    """
    # L1
    haircuts_per_free = 14 # For every 14 haircuts, she gets a free additional haircut
    num_free_haircuts = 5 # She has gotten 5 free haircuts already
    haircuts_for_free = haircuts_per_free * num_free_haircuts

    # L2
    haircuts_away_from_next_free = 5 # She is 5 haircuts away from another free one
    haircuts_towards_next_free = haircuts_per_free - haircuts_away_from_next_free

    # L3
    total_haircuts = haircuts_for_free + haircuts_towards_next_free

    # FA
    answer = total_haircuts
    return answer