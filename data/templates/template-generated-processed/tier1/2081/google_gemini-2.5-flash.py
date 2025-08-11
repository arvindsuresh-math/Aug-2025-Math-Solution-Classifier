def solve():
    """Index: 2081.
    Returns: the total number of days Cassidy is grounded for.
    """
    # L1
    num_grades_below_B = 4 # four grades below a B
    days_per_grade_below_B = 3 # 3 extra days for each grade below a B
    grounding_for_low_grades = num_grades_below_B * days_per_grade_below_B

    # L2
    base_grounding_days = 14 # grounded for 14 days for lying about her report card
    total_grounding_days = grounding_for_low_grades + base_grounding_days

    # FA
    answer = total_grounding_days
    return answer