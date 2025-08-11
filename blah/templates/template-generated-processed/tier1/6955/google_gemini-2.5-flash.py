def solve():
    """Index: 6955.
    Returns: the duration Carlo should practice on Friday in minutes.
    """
    # L1
    thursday_practice_minutes = 50 # On Thursday, he practiced for 50 minutes
    wednesday_more_than_thursday = 5 # 5 minutes more than on Thursday
    wednesday_practice_minutes = thursday_practice_minutes + wednesday_more_than_thursday

    # L2
    tuesday_less_than_wednesday = 10 # 10 minutes less than on Wednesday
    tuesday_practice_minutes = wednesday_practice_minutes - tuesday_less_than_wednesday

    # L3
    monday_multiplier = 2 # practiced twice as long on Monday as on Tuesday
    monday_practice_minutes = tuesday_practice_minutes * monday_multiplier

    # L4
    total_practice_mon_thu = monday_practice_minutes + tuesday_practice_minutes + wednesday_practice_minutes + thursday_practice_minutes

    # L5
    total_hours_needed = 5 # practice for a total of 5 hours
    minutes_per_hour = 60 # WK
    total_minutes_needed = minutes_per_hour * total_hours_needed

    # L6
    friday_practice_minutes = total_minutes_needed - total_practice_mon_thu

    # FA
    answer = friday_practice_minutes
    return answer