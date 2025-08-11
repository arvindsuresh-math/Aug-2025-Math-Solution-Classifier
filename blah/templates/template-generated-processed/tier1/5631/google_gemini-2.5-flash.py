def solve():
    """Index: 5631.
    Returns: the total hours of classes Kim has per day.
    """
    # L1
    initial_classes = 4 # 4 classes in school
    dropped_classes = 1 # drops 1 class
    remaining_classes = initial_classes - dropped_classes

    # L2
    hours_per_class = 2 # 2 hours each
    total_hours = remaining_classes * hours_per_class

    # FA
    answer = total_hours
    return answer