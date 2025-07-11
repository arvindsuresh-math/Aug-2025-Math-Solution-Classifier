def solve():
    """Index: 1166.
    Returns: the number of crickets the gecko eats on the third day.
    """
    # L1
    total_crickets = 70 # eats 70 crickets every three days
    first_day_percent = 0.30 # eats 30% of the crickets
    first_day_crickets = total_crickets * first_day_percent

    # L2
    second_day_subtract = 6 # eats 6 less than the first
    second_day_crickets = first_day_crickets - second_day_subtract

    # L3
    third_day_crickets = total_crickets - first_day_crickets - second_day_crickets

    # FA
    answer = third_day_crickets
    return answer