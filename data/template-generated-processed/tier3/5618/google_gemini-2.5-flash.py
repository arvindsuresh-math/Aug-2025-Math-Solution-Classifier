def solve():
    """Index: 5618.
    Returns: the average number of hours Harry sleeps in one night.
    """
    # L1
    monday_sleep_hours = 8 # sleeps for 8 hours
    tuesday_sleep_hours = 7 # sleeps for 7 hours
    wednesday_sleep_hours = 8 # sleeps for 8 hours
    thursday_sleep_hours = 10 # sleeps for 10 hours
    friday_sleep_hours = 7 # sleeps for 7 hours
    total_sleep_hours = monday_sleep_hours + tuesday_sleep_hours + wednesday_sleep_hours + thursday_sleep_hours + friday_sleep_hours

    # L2
    number_of_days = 5 # Monday through Friday

    # L3
    average_sleep_hours = total_sleep_hours / number_of_days

    # FA
    answer = average_sleep_hours
    return answer