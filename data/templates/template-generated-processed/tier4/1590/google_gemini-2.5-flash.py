def solve():
    """Index: 1590.
    Returns: the amount of money John saves per day.
    """
    # L1
    initial_coffees_per_day = 4 # 4 coffees a day
    cut_coffees_divisor = 2 # cut the number of coffees he drinks in half
    new_coffees_per_day = initial_coffees_per_day / cut_coffees_divisor

    # L2
    old_coffee_price = 2 # $2 each
    price_increase_percent = 0.5 # raised the price by 50%
    price_increase_amount = old_coffee_price * price_increase_percent

    # L3
    new_coffee_price = old_coffee_price + price_increase_amount

    # L4
    new_daily_spend = new_coffee_price * new_coffees_per_day

    # L5
    old_daily_spend = initial_coffees_per_day * old_coffee_price

    # L6
    daily_savings = old_daily_spend - new_daily_spend

    # FA
    answer = daily_savings
    return answer