def solve():
    """Index: 7404.
    Returns: the total cost to look for an item for 10 days.
    """
    # L1
    initial_days_count = 5 # for the first 5 days
    fee_initial_days = 100 # $100 a day
    cost_initial_days = initial_days_count * fee_initial_days

    # L2
    total_days = 10 # for 10 days
    discount_days = total_days - initial_days_count

    # L3
    fee_after_initial = 60 # $60 per day for every day after that
    cost_discounted_days = discount_days * fee_after_initial

    # L4
    total_cost = cost_initial_days + cost_discounted_days

    # FA
    answer = total_cost
    return answer