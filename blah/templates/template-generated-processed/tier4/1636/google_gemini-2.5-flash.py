def solve():
    """Index: 1636.
    Returns: the average number of minutes Keegan spends in one of his other classes.
    """
    # L1
    total_classes = 7 # taking 7 classes
    known_classes = 2 # history and chemistry classes
    other_classes_count = total_classes - known_classes

    # L2
    total_school_hours = 7.5 # 7.5 hours each day
    known_classes_duration_hours = 1.5 # combined total of 1.5 hours
    remaining_hours = total_school_hours - known_classes_duration_hours

    # L3
    minutes_per_hour = 60 # WK
    remaining_minutes = remaining_hours * minutes_per_hour

    # L4
    average_minutes_per_other_class = remaining_minutes / other_classes_count

    # FA
    answer = average_minutes_per_other_class
    return answer