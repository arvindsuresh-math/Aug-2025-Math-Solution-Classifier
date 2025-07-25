def solve():
    """Index: 4343.
    Returns: the number of pancakes Janina must sell each day to cover her expenses.
    """
    # L1
    rent_cost = 30 # spends $30 each day for rent
    supplies_cost = 12 # uses $12 worth of supplies daily
    total_daily_expenses = rent_cost + supplies_cost

    # L2
    pancake_price = 2 # sells each pancake for $2
    pancakes_needed = total_daily_expenses / pancake_price

    # FA
    answer = pancakes_needed
    return answer