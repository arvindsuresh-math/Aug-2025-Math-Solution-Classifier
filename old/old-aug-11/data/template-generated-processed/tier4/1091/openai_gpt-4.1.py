def solve():
    """Index: 1091.
    Returns: the total amount Harper will spend on mineral water for 240 days.
    """
    # L1
    bottles_per_case = 24 # 24 bottles to a case
    bottles_per_day = 0.5 # 1/2 bottle of mineral water per day
    days_per_case = bottles_per_case / bottles_per_day

    # L2
    total_days = 240 # 240 days
    cases_needed = total_days / days_per_case

    # L3
    price_per_case = 12.00 # $12.00 per case
    total_cost = price_per_case * cases_needed

    # FA
    answer = total_cost
    return answer