def solve():
    """Index: 2418.
    Returns: the amount left on Lyra's weekly food budget after her purchases.
    """
    # L1
    beef_pounds = 5 # 5 pounds of beef
    beef_price_per_pound = 3 # $3 per pound
    beef_total = beef_price_per_pound * beef_pounds

    # L2
    chicken_price = 12 # 1 bucket of fried chicken that costs $12
    total_spent = chicken_price + beef_total

    # L3
    budget = 80 # $80 budget for a week
    amount_left = budget - total_spent

    # FA
    answer = amount_left
    return answer