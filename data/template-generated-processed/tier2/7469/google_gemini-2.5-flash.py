def solve():
    """Index: 7469.
    Returns: the cost of the box of cookies.
    """
    # L1
    sell_price_per_bracelet = 1.5 # sells each one for $1.5
    cost_per_bracelet = 1 # costs $1 for supplies for each bracelet
    profit_per_bracelet = sell_price_per_bracelet - cost_per_bracelet

    # L2
    num_bracelets = 12 # makes 12 bracelets
    total_earnings = num_bracelets * profit_per_bracelet

    # L3
    remaining_money = 3 # still has $3
    cost_of_cookies = total_earnings - remaining_money

    # FA
    answer = cost_of_cookies
    return answer