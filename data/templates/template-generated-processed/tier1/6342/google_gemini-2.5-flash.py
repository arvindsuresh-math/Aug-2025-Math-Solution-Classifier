def solve():
    """Index: 6342.
    Returns: the total number of customers seen during the holiday season in 8 hours.
    """
    # L1
    people_per_hour_normal = 175 # 175 people enter their store every hour
    doubling_factor = 2 # This number doubles
    people_per_hour_holiday = people_per_hour_normal * doubling_factor

    # L2
    hours_in_day = 8 # in 8 hours
    total_customers_holiday = hours_in_day * people_per_hour_holiday

    # FA
    answer = total_customers_holiday
    return answer