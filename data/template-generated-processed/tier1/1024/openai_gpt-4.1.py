def solve():
    """Index: 1024.
    Returns: the total amount of money Rafael makes in a week.
    """
    # L1
    monday_hours = 10 # works 10 hours on Monday
    tuesday_hours = 8 # 8 hours on Tuesday
    hours_worked_by_tuesday = tuesday_hours + monday_hours

    # L2
    hours_left = 20 # 20 hours left to work in the week
    total_weekly_hours = hours_worked_by_tuesday + hours_left

    # L3
    pay_per_hour = 20 # paid $20 per hour
    total_pay = pay_per_hour * total_weekly_hours

    # FA
    answer = total_pay
    return answer