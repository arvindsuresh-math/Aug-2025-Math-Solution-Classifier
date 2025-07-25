def solve():
    """Index: 3720.
    Returns: the average number of pastries sold per day.
    """
    # L1
    monday_sales = 2 # On Monday he sold 2
    sales_increase_per_day = 1 # Every day the number of sales increases by 1 compared to the previous day
    tuesday_sales = monday_sales + sales_increase_per_day
    wednesday_sales = tuesday_sales + sales_increase_per_day
    thursday_sales = wednesday_sales + sales_increase_per_day
    friday_sales = thursday_sales + sales_increase_per_day
    saturday_sales = friday_sales + sales_increase_per_day
    sunday_sales = saturday_sales + sales_increase_per_day

    # L2
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales + friday_sales + saturday_sales + sunday_sales
    days_in_week = 7 # works 7 days a week

    # L3
    average_sales = total_sales / days_in_week

    # FA
    answer = average_sales
    return answer