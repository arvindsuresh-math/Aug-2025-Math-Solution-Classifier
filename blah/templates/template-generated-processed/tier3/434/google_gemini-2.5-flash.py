def solve():
    """Index: 434.
    Returns: the percentage Calvin is towards his goal.
    """
    # L1
    haircuts_had = 8 # He has gotten 8 haircuts
    haircuts_needed_more = 2 # needs 2 more
    total_haircuts_goal = haircuts_had + haircuts_needed_more

    # L2
    percentage_multiplier = 100 # WK
    percentage_towards_goal = (haircuts_had / total_haircuts_goal) * percentage_multiplier

    # FA
    answer = percentage_towards_goal
    return answer