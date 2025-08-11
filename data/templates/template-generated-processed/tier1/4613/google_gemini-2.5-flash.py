def solve():
    """Index: 4613.
    Returns: the total dollars saved for the trip.
    """
    # L1
    num_students = 30 # A class of 30 high school students
    contribution_per_student_per_week = 2 # $2 every Friday
    weekly_savings = num_students * contribution_per_student_per_week

    # L2
    num_months = 2 # in 2 months
    weeks_per_month = 4 # WK
    total_weeks = num_months * weeks_per_month

    # L3
    total_savings = weekly_savings * total_weeks

    # FA
    answer = total_savings
    return answer