def solve():
    """Index: 2027.
    Returns: the total temperature of the remaining days of that week.
    """
    # L1
    average_temp_week = 60 # The average temperature in Orlando in a particular week was 60 degrees
    days_in_week = 7 # WK
    total_temp_week = days_in_week * average_temp_week

    # L2
    num_first_days = 3 # first 3 days
    temp_first_days = 40 # temperature on each of the first 3 days in that week was 40
    total_temp_first_three_days = num_first_days * temp_first_days

    # L3
    temp_thu_fri = 80 # temperature for Thursday and Friday was 80 degrees each
    num_thu_fri_days = 2 # WK
    total_temp_thu_fri = temp_thu_fri * num_thu_fri_days

    # L4
    total_temp_first_five_days = total_temp_thu_fri + total_temp_first_three_days

    # L5
    total_temp_remaining_days = total_temp_week - total_temp_first_five_days

    # FA
    answer = total_temp_remaining_days
    return answer