def solve():
    """Index: 6860.
    Returns: Calvin's weight after one year of training.
    """
    # L1
    pounds_lost_per_month = 8 # lost 8 pounds every month
    months_per_year = 12 # WK
    total_pounds_lost = months_per_year * pounds_lost_per_month

    # L2
    initial_weight = 250 # weighed 250 pounds to start with
    final_weight = initial_weight - total_pounds_lost

    # FA
    answer = final_weight
    return answer