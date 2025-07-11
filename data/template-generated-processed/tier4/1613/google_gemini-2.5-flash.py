def solve():
    """Index: 1613.
    Returns: the total sales per week.
    """
    # L1
    total_houses_per_day = 50 # He visits 50 houses a day
    buying_percentage = 0.2 # 20% of them buy something
    buying_houses_per_day = total_houses_per_day * buying_percentage

    # L2
    knife_set_types = 2 # half buy a $50 set of knives and the other half buy a $150 set of knives
    houses_per_knife_type = buying_houses_per_day / knife_set_types

    # L3
    cheap_knife_price = 50 # $50 set of knives
    daily_sales_cheap_set = houses_per_knife_type * cheap_knife_price

    # L4
    expensive_knife_price = 150 # $150 set of knives
    daily_sales_expensive_set = houses_per_knife_type * expensive_knife_price

    # L5
    total_daily_sales = daily_sales_cheap_set + daily_sales_expensive_set

    # L6
    working_days_per_week = 5 # works 5 days a week
    total_weekly_sales = total_daily_sales * working_days_per_week

    # FA
    answer = total_weekly_sales
    return answer