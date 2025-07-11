def solve():
    """Index: 2712.
    Returns: the total amount of money the teacher earns in 5 weeks.
    """
    # L1
    half_hour_lesson_cost = 10 # $10 for every half-hour
    hours_per_lesson = 1 # lesson lasts 1 hour
    half_hours_per_lesson = 2 # 1 hour = 2 half-hours (WK)
    one_hour_lesson_cost = half_hours_per_lesson * half_hour_lesson_cost

    # L2
    num_weeks = 5 # in 5 weeks
    total_earnings = one_hour_lesson_cost * num_weeks

    # FA
    answer = total_earnings
    return answer