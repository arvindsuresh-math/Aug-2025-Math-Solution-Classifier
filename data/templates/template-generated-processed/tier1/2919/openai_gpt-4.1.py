def solve():
    """Index: 2919.
    Returns: the number of people who can take classes in 3 weeks.
    """
    # L1
    weekday_classes_per_day = 2 # 2 beginning diving classes on weekdays
    num_weekdays = 5 # weekdays
    weekday_classes = weekday_classes_per_day * num_weekdays

    # L2
    weekend_classes_per_day = 4 # 4 beginning classes on each day of the weekend
    num_weekend_days = 2 # weekend
    weekend_classes = weekend_classes_per_day * num_weekend_days

    # L3
    total_classes_per_week = weekday_classes + weekend_classes

    # L4
    people_per_class = 5 # Each class has room for 5 people
    people_per_week = total_classes_per_week * people_per_class

    # L5
    num_weeks = 3 # in 3 weeks
    answer = people_per_week * num_weeks
    return answer