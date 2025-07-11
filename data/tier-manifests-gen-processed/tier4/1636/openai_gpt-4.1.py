def solve():
    """Index: 1636.
    Returns: the average number of minutes Keegan spends in one of his other classes.
    """
    # L1
    total_classes = 7 # Keegan is taking 7 classes
    history_chemistry_classes = 2 # history and chemistry classes
    other_classes = total_classes - history_chemistry_classes

    # L2
    total_hours = 7.5 # Keegan is in school for 7.5 hours each day
    history_chemistry_hours = 1.5 # history and chemistry classes for a combined total of 1.5 hours
    other_classes_hours = total_hours - history_chemistry_hours

    # L3
    minutes_per_hour = 60 # WK
    other_classes_minutes = other_classes_hours * minutes_per_hour

    # L4
    avg_minutes_per_other_class = other_classes_minutes / other_classes

    # FA
    answer = avg_minutes_per_other_class
    return answer