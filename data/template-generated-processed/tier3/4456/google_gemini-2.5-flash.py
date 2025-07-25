def solve():
    """Index: 4456.
    Returns: the total number of classes in the school.
    """
    # L1
    sheets_per_class_per_day = 200 # Each class uses 200 sheets of paper per day
    school_days_per_week = 5 # 5 days of school days
    sheets_per_class_per_week = sheets_per_class_per_day * school_days_per_week

    # L2
    total_sheets_per_week = 9000 # The school uses a total of 9000 sheets of paper every week
    number_of_classes = total_sheets_per_week / sheets_per_class_per_week

    # FA
    answer = number_of_classes
    return answer