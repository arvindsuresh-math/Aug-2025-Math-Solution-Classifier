def solve():
    """Index: 4817.
    Returns: the amount Jeff paid when picking up the costume.
    """
    # L1
    last_year_cost = 250 # which cost $250
    cost_increase_percent = 0.4 # 40% more expensive
    cost_increase_amount = last_year_cost * cost_increase_percent

    # L2
    current_cost = last_year_cost + cost_increase_amount

    # L3
    deposit_percent = 0.1 # 10% deposit
    deposit_amount = current_cost * deposit_percent

    # L4
    amount_paid_at_pickup = current_cost - deposit_amount

    # FA
    answer = amount_paid_at_pickup
    return answer