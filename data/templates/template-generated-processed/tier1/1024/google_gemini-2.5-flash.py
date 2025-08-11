def solve():
    """Index: 1024.
    Returns: the total money Rafael makes in a week.
    """
    # L1
    hours_tuesday = 8 # 8 hours on Tuesday
    hours_monday = 10 # 10 hours on Monday
    hours_worked_by_tuesday = hours_tuesday + hours_monday

    # L2
    hours_left_to_work = 20 # 20 hours left to work in the week
    total_weekly_hours = hours_worked_by_tuesday + hours_left_to_work

    # L3
    pay_per_hour = 20 # $20 per hour
    total_money_made = pay_per_hour * total_weekly_hours

    # FA
    answer = total_money_made
    return answer