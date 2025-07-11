def solve():
    """Index: 2427.
    Returns: the average amount of beef sold per day.
    """
    # L1
    thursday_sales = 210 # On Thursday Walmart sold 210 pounds of ground beef
    friday_multiplier = 2 # On Friday they sold twice that amount
    friday_sales = friday_multiplier * thursday_sales

    # L2
    saturday_sales = 150 # On Saturday they only sold 150 pounds
    total_sales = thursday_sales + friday_sales + saturday_sales

    # L3
    number_of_days = 3 # per day (Thursday, Friday, Saturday are 3 days)
    average_sales = total_sales / number_of_days

    # FA
    answer = average_sales
    return answer