def solve():
    """Index: 2081.
    Returns: the total number of days Cassidy is grounded for.
    """
    # L1
    num_grades_below_B = 4 # four grades below a B
    extra_days_per_grade = 3 # 3 extra days for each grade below a B
    extra_days = num_grades_below_B * extra_days_per_grade

    # L2
    base_days = 14 # grounded for 14 days for lying about her report card
    total_days = extra_days + base_days

    # FA
    answer = total_days
    return answer