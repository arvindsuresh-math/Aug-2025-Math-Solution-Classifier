def solve():
    """Index: 1633.
    Returns: the number of weeks it took to finish all the chocolate.
    """
    # L1
    weekdays_per_week = 5 # WK
    chocolates_per_weekday = 2 # Erwin eats 2 chocolates on weekdays
    chocolates_on_weekdays = weekdays_per_week * chocolates_per_weekday

    # L2
    weekend_days_per_week = 2 # WK
    chocolates_per_weekend_day = 1 # and 1 chocolate on weekends
    chocolates_on_weekends = weekend_days_per_week * chocolates_per_weekend_day

    # L3
    total_chocolates_per_week = chocolates_on_weekdays + chocolates_on_weekends

    # L4
    total_chocolates_eaten = 24 # He ate 24 chocolates in total
    weeks_to_finish = total_chocolates_eaten / total_chocolates_per_week

    # FA
    answer = weeks_to_finish
    return answer