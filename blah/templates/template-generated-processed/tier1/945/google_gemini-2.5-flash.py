def solve():
    """Index: 945.
    Returns: the total amount Jon spends in April.
    """
    # L1
    coffees_per_day = 2 # 2 coffees a day
    cost_per_coffee = 2 # $2 each
    daily_spend = coffees_per_day * cost_per_coffee

    # L2
    days_in_april = 30 # WK
    total_spend_april = daily_spend * days_in_april

    # FA
    answer = total_spend_april
    return answer