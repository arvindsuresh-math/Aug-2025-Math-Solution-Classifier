def solve():
    """Index: 4044.
    Returns: the total money Janice makes in a week.
    """
    # L1
    regular_rate = 10 # $10 an hour
    regular_hours_limit = 40 # for the first 40 hours she works each week
    regular_pay = regular_rate * regular_hours_limit

    # L2
    total_hours_worked = 60 # works 60 hours one week
    overtime_hours = total_hours_worked - regular_hours_limit

    # L3
    overtime_rate = 15 # $15 each hour of overtime
    overtime_pay = overtime_rate * overtime_hours

    # L4
    total_weekly_pay = regular_pay + overtime_pay

    # FA
    answer = total_weekly_pay
    return answer