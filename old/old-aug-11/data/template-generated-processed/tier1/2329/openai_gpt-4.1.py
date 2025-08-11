def solve():
    """Index: 2329.
    Returns: the total cost for Archie to buy antibiotics for a week.
    """
    # L1
    antibiotic_cost = 3 # antibiotic costs $3 each
    antibiotics_per_day = 3 # take antibiotics three times a day
    daily_cost = antibiotic_cost * antibiotics_per_day

    # L2
    days_in_week = 7 # WK
    total_cost = daily_cost * days_in_week

    # FA
    answer = total_cost
    return answer