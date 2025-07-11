def solve():
    """Index: 1059.
    Returns: the total number of juice boxes needed for the entire school year.
    """
    # L1
    num_children = 3 # 3 children
    days_per_week = 5 # 5 days a week
    juice_boxes_per_week = num_children * days_per_week

    # L2
    school_year_weeks = 25 # 25 weeks long
    total_juice_boxes = school_year_weeks * juice_boxes_per_week

    # FA
    answer = total_juice_boxes
    return answer