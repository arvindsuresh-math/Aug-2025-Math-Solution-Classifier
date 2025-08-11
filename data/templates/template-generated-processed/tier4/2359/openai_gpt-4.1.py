def solve():
    """Index: 2359.
    Returns: the profit in cents Joshua will make on each orange.
    """
    # L1
    dollars_per_cent = 100 # WK
    total_dollars = 12.50 # $12.50
    total_cents = dollars_per_cent * total_dollars

    # L2
    num_oranges = 25 # 25 oranges
    cost_per_orange = total_cents / num_oranges

    # L3
    sell_price_per_orange = 60 # sells each one for 60c
    profit_per_orange = sell_price_per_orange - cost_per_orange

    # FA
    answer = profit_per_orange
    return answer