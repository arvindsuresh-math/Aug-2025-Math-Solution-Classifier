def solve():
    """Index: 1166.
    Returns: the number of crickets the gecko eats on the third day.
    """
    # L1
    total_crickets = 70 # eats 70 crickets
    day1_percent_decimal = 0.30 # eats 30% of the crickets
    day1_crickets = total_crickets * day1_percent_decimal

    # L2
    day2_less_than_day1 = 6 # eats 6 less than the first
    day2_crickets = day1_crickets - day2_less_than_day1

    # L3
    day3_crickets = total_crickets - day1_crickets - day2_crickets

    # FA
    answer = day3_crickets
    return answer