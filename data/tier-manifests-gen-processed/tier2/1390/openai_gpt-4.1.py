def solve():
    """Index: 1390.
    Returns: the total amount Nancy has spent on coffee after 20 days.
    """
    # L1
    double_espresso_price = 3.00 # double espresso for $3.00 every morning
    iced_coffee_price = 2.50 # iced coffee for $2.50 in the afternoon
    daily_coffee_spend = double_espresso_price + iced_coffee_price

    # L2
    num_days = 20 # after 20 days
    total_spent = num_days * daily_coffee_spend

    # FA
    answer = total_spent
    return answer