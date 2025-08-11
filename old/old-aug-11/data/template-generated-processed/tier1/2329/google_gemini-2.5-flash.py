def solve():
    """Index: 2329.
    Returns: the total money needed to buy the antibiotics for a week.
    """
    # L1
    antibiotic_cost_per_pill = 3 # antibiotic costs $3 each
    times_per_day = 3 # take antibiotics three times a day
    cost_per_day = antibiotic_cost_per_pill * times_per_day

    # L2
    days_in_week = 7 # WK
    total_cost = cost_per_day * days_in_week

    # FA
    answer = total_cost
    return answer