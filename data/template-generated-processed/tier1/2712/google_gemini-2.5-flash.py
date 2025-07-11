def solve():
    """Index: 2712.
    Returns: the total money the teacher would earn in 5 weeks.
    """
    # L1
    cost_per_half_hour = 10 # $10 for every half-hour of teaching
    half_hours_per_hour = 2 # WK
    cost_per_hour_lesson = half_hours_per_hour * cost_per_half_hour

    # L2
    num_weeks = 5 # in 5 weeks
    total_earnings = cost_per_hour_lesson * num_weeks

    # FA
    answer = total_earnings
    return answer