def solve():
    """Index: 1390.
    Returns: the total money spent on coffee.
    """
    # L1
    espresso_cost = 3.00 # $3.00 every morning
    iced_coffee_cost = 2.50 # $2.50
    daily_coffee_cost = espresso_cost + iced_coffee_cost

    # L2
    num_days = 20 # After 20 days
    total_coffee_cost = num_days * daily_coffee_cost

    # FA
    answer = total_coffee_cost
    return answer