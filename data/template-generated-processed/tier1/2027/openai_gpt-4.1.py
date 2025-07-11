def solve():
    """Index: 2027.
    Returns: the total temperature of the remaining days of the week.
    """
    # L1
    days_in_week = 7 # WK
    avg_temp = 60 # average temperature in Orlando in a particular week was 60 degrees
    total_temp_week = days_in_week * avg_temp

    # L2
    first_three_days = 3 # first 3 days
    temp_first_three = 40 # temperature on each of the first 3 days in that week was 40
    total_temp_first_three = first_three_days * temp_first_three

    # L3
    thurs_fri_days = 2 # Thursday and Friday
    temp_thurs_fri = 80 # temperature for Thursday and Friday was 80 degrees each
    total_temp_thurs_fri = temp_thurs_fri * thurs_fri_days

    # L4
    total_temp_first_five = total_temp_thurs_fri + total_temp_first_three

    # L5
    total_temp_remaining = total_temp_week - total_temp_first_five

    # FA
    answer = total_temp_remaining
    return answer