def solve():
    """Index: 1059.
    Returns: the total number of juice boxes needed for the school year for all children.
    """
    # L1
    num_children = 3 # Peyton has 3 children
    juice_boxes_per_child_per_day = 1 # each get a juice box in their lunch
    days_per_week = 5 # 5 days a week
    juice_boxes_per_week = num_children * days_per_week

    # L2
    weeks_in_school_year = 25 # The school year is 25 weeks long
    total_juice_boxes = weeks_in_school_year * juice_boxes_per_week

    # FA
    answer = total_juice_boxes
    return answer