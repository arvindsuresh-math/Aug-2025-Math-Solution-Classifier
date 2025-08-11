def solve():
    """Index: 3260.
    Returns: the amount Martha will save on coffee spending.
    """
    # L1
    latte_price = 4.00 # $4.00 every morning
    latte_days_per_week = 5 # 5 days a week
    weekly_latte_cost = latte_price * latte_days_per_week

    # L2
    iced_coffee_price = 2.00 # $2.00
    iced_coffee_days_per_week = 3 # 3 days a week
    weekly_iced_coffee_cost = iced_coffee_price * iced_coffee_days_per_week

    # L3
    total_weekly_spending = weekly_latte_cost + weekly_iced_coffee_cost

    # L4
    weeks_per_year = 52 # 52 weeks
    annual_spending = weeks_per_year * total_weekly_spending

    # L5
    spending_cut_percent_decimal = 0.25 # cut her coffee spending by 25%
    spending_cut_percent_text = 25 # cut her coffee spending by 25%
    amount_saved = spending_cut_percent_decimal * annual_spending

    # FA
    answer = amount_saved
    return answer