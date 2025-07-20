def solve():
    """Index: 4668.
    Returns: the average hours of homework Paul needs to do per night.
    """
    # L1
    hours_per_weeknight = 2 # 2 hours of homework on weeknights
    weeknights_in_week = 5 # WK
    total_weeknight_homework = hours_per_weeknight * weeknights_in_week

    # L2
    weekend_homework = 5 # 5 hours for the entire weekend
    total_homework_hours = weekend_homework + total_weeknight_homework

    # L3
    days_in_week = 7 # WK
    practice_nights = 2 # practice 2 nights out of the week
    available_homework_nights = days_in_week - practice_nights

    # L4
    average_hours_per_night = total_homework_hours / available_homework_nights

    # FA
    answer = average_hours_per_night
    return answer