def solve():
    """Index: 2971.
    Returns: the number of additional flies Betty needs to gather a week's food for her frog.
    """
    # L1
    flies_per_day = 2 # frog eats 2 flies per day
    days_per_week = 7 # WK
    flies_per_week = flies_per_day * days_per_week

    # L2
    flies_morning = 5 # catches 5 flies in the morning
    flies_afternoon = 6 # catches 6 more in the afternoon
    total_caught = flies_morning + flies_afternoon

    # L3
    flies_escaped = 1 # 1 escapes
    flies_remaining = total_caught - flies_escaped

    # L4
    flies_needed = flies_per_week - flies_remaining

    # FA
    answer = flies_needed
    return answer