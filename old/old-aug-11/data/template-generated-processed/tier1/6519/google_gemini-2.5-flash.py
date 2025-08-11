def solve():
    """Index: 6519.
    Returns: the total number of apple snails eaten over 5 days.
    """
    # L1
    snails_day1 = 3 # ate 3 snails
    daily_increase = 2 # eats 2 more snails than it did the day before
    snails_day2 = snails_day1 + daily_increase

    # L2
    snails_day3 = snails_day2 + daily_increase

    # L3
    snails_day4 = snails_day3 + daily_increase

    # L4
    snails_day5 = snails_day4 + daily_increase

    # L5
    total_snails = snails_day1 + snails_day2 + snails_day3 + snails_day4 + snails_day5

    # FA
    answer = total_snails
    return answer