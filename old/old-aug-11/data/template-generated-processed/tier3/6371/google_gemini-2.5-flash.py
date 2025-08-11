def solve():
    """Index: 6371.
    Returns: the number of days' worth of profits to pay for the cash register.
    """
    # L1
    loaves_sold_daily = 40 # 40 loaves of bread
    price_per_loaf = 2 # $2 each
    daily_bread_income = loaves_sold_daily * price_per_loaf

    # L2
    cakes_sold_daily = 6 # 6 cakes
    price_per_cake = 12 # $12 each
    daily_cake_income = cakes_sold_daily * price_per_cake

    # L3
    total_daily_income = daily_bread_income + daily_cake_income

    # L4
    daily_rent = 20 # $20 each day for rent
    daily_electricity = 2 # $2 each day for electricity
    daily_profit = total_daily_income - daily_rent - daily_electricity

    # L5
    cash_register_cost = 1040 # costs $1040
    days_to_pay = cash_register_cost / daily_profit

    # FA
    answer = days_to_pay
    return answer