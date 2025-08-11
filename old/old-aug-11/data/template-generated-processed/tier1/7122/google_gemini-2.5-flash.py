def solve():
    """Index: 7122.
    Returns: the total amount Mark spent.
    """
    # L1
    pounds_tomatoes = 2 # 2 pounds of tomatoes
    price_per_pound_tomatoes = 5 # $5 per pound
    cost_tomatoes = pounds_tomatoes * price_per_pound_tomatoes

    # L2
    pounds_apples = 5 # 5 pounds of apples
    price_per_pound_apples = 6 # $6 per pound
    cost_apples = price_per_pound_apples * pounds_apples

    # L3
    total_spending = cost_apples + cost_tomatoes

    # FA
    answer = total_spending
    return answer