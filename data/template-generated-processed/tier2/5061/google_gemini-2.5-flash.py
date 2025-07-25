def solve():
    """Index: 5061.
    Returns: the number of hours per week Ruth spends in math class.
    """
    # L1
    days_per_week = 5 # 5 days a week
    hours_per_day = 8 # 8 hours a day
    total_school_hours_per_week = days_per_week * hours_per_day

    # L2
    math_class_percentage_decimal = 0.25 # 25% of this time
    math_class_hours_per_week = total_school_hours_per_week * math_class_percentage_decimal

    # FA
    answer = math_class_hours_per_week
    return answer