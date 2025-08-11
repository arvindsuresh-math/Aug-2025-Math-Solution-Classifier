def solve():
    """Index: 1613.
    Returns: the total amount John sells in a week.
    """
    # L1
    houses_per_day = 50 # John visits 50 houses a day
    buy_percent = 0.2 # 20% of them buy something
    houses_buying_per_day = houses_per_day * buy_percent

    # L2
    buyers_per_type = houses_buying_per_day / 2 # half buy each type

    # L3
    cheap_set_price = 50 # $50 set of knives
    cheap_set_sales_per_day = buyers_per_type * cheap_set_price

    # L4
    expensive_set_price = 150 # $150 set of knives
    expensive_set_sales_per_day = buyers_per_type * expensive_set_price

    # L5
    total_sales_per_day = cheap_set_sales_per_day + expensive_set_sales_per_day

    # L6
    days_per_week = 5 # he works 5 days a week
    total_sales_per_week = total_sales_per_day * days_per_week

    # FA
    answer = total_sales_per_week
    return answer