def solve():
    """Index: 2359.
    Returns: the profit in cents made on each orange.
    """
    # L1
    dollars_to_cents_factor = 100 # WK
    total_cost_dollars = 12.50 # $12.50
    total_cost_cents = dollars_to_cents_factor * total_cost_dollars

    # L2
    num_oranges = 25 # 25 oranges
    cost_per_orange_cents = total_cost_cents / num_oranges

    # L3
    selling_price_per_orange_cents = 60 # sells each one for 60c
    profit_per_orange_cents = selling_price_per_orange_cents - cost_per_orange_cents

    # FA
    answer = profit_per_orange_cents
    return answer