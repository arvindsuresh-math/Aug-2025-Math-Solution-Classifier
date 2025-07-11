def solve():
    """Index: 1091.
    Returns: the total amount Harper will spend.
    """
    # L1
    daily_consumption = 0.5 # 1/2 bottle of mineral water per day
    bottles_per_case = 24 # 24 bottles to a case
    days_per_case = bottles_per_case / daily_consumption

    # L2
    desired_duration_days = 240 # last her 240 days
    num_cases_needed = desired_duration_days / days_per_case

    # L3
    cost_per_case = 12.00 # $12.00
    total_cost = cost_per_case * num_cases_needed

    # FA
    answer = total_cost
    return answer