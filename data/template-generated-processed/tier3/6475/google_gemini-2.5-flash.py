def solve():
    """Index: 6475.
    Returns: the number of marbles Cruz has.
    """
    # L1
    total_sum_multiplied_by_three = 60 # Three times the sum of marbles that Atticus, Jensen, and Cruz have is equal to 60
    multiplier = 3 # Three times the sum
    total_marbles_all_three = total_sum_multiplied_by_three / multiplier

    # L2
    atticus_marbles = 4 # Atticus has 4 marbles
    ratio_atticus_to_jensen = 2 # Atticus has half as many marbles as Jensen
    jensen_marbles = ratio_atticus_to_jensen * atticus_marbles

    # L3
    atticus_jensen_total = jensen_marbles + atticus_marbles

    # L4
    cruz_marbles = total_marbles_all_three - atticus_jensen_total

    # FA
    answer = cruz_marbles
    return answer