def solve():
    """Index: 2919.
    Returns: the total number of people who can take classes in 3 weeks.
    """
    # L1
    weekday_classes_offered = 2 # 2 beginning diving classes on weekdays
    weekday_days_in_week = 5 # WK
    total_weekday_classes = weekday_classes_offered * weekday_days_in_week

    # L2
    weekend_classes_offered = 4 # 4 beginning classes on each day of the weekend
    weekend_days_in_week = 2 # WK
    total_weekend_classes = weekend_classes_offered * weekend_days_in_week

    # L3
    total_classes_per_week = total_weekday_classes + total_weekend_classes

    # L4
    room_per_class = 5 # room for 5 people
    people_per_week = total_classes_per_week * room_per_class

    # L5
    number_of_weeks = 3 # in 3 weeks
    total_people_in_3_weeks = people_per_week * number_of_weeks

    # FA
    answer = total_people_in_3_weeks
    return answer