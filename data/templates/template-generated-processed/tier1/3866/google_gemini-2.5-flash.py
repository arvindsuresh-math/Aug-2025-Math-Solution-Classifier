def solve():
    """Index: 3866.
    Returns: the original number of bikes the shop owner had.
    """
    # L2
    bikes_added_per_week = 3 # adds 3 bikes to her stock every week
    weeks_per_month = 4 # WK
    total_bikes_added = bikes_added_per_week * weeks_per_month

    # L6
    bikes_in_stock_final = 45 # still had 45 bikes in stock
    bikes_sold = 18 # sold 18 bikes
    original_bikes = bikes_in_stock_final - total_bikes_added + bikes_sold

    # FA
    answer = original_bikes
    return answer