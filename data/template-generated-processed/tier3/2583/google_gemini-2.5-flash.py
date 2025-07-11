def solve():
    """Index: 2583.
    Returns: the amount Cindy earned for teaching 1 math course in a month.
    """
    # L1
    total_weekly_hours = 48 # 48 hours a week altogether
    num_courses = 4 # 4 math courses
    hours_per_course_per_week = total_weekly_hours / num_courses

    # L2
    weeks_per_month = 4 # month with exactly 4 weeks
    hours_per_course_per_month = hours_per_course_per_week * weeks_per_month

    # L3
    hourly_rate = 25 # hourly rate per class is $25
    monthly_earnings_per_course = hourly_rate * hours_per_course_per_month

    # FA
    answer = monthly_earnings_per_course
    return answer