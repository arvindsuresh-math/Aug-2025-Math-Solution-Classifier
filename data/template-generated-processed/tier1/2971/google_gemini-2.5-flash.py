def solve():
    """Index: 2971.
    Returns: the number of more flies Betty needs for the week.
    """
    # L1
    flies_per_day = 2 # eats 2 flies
    days_per_week = 7 # WK
    flies_needed_per_week = flies_per_day * days_per_week

    # L2
    flies_morning = 5 # catches 5 flies
    flies_afternoon = 6 # catches 6 more
    flies_caught_total = flies_morning + flies_afternoon

    # L3
    flies_escaped = 1 # one escapes
    flies_remaining = flies_caught_total - flies_escaped

    # L4
    flies_needed_more = flies_needed_per_week - flies_remaining

    # FA
    answer = flies_needed_more
    return answer