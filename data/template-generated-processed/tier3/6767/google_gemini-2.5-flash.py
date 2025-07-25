def solve():
    """Index: 6767.
    Returns: the number of pages Jenna needs to read per day.
    """
    # L1
    days_in_september = 30 # September (which has 30 days)
    days_cant_read = 4 # four weekdays starting on the 13th, so she won't have time to read
    reading_days_after_busy_period = days_in_september - days_cant_read

    # L2
    flight_day_count = 1 # 100 pages on the 23rd
    remaining_reading_days = reading_days_after_busy_period - flight_day_count

    # L3
    overall_goal_pages = 600 # goal of reading 600 pages a month
    pages_on_flight = 100 # read 100 pages on the 23rd
    pages_remaining_after_flight = overall_goal_pages - pages_on_flight

    # L4
    pages_per_day = pages_remaining_after_flight / remaining_reading_days

    # FA
    answer = pages_per_day
    return answer