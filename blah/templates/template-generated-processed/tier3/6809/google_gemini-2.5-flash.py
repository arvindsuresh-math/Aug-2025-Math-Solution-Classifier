def solve():
    """Index: 6809.
    Returns: the total amount of money Jerry would earn at the end of the week.
    """
    # L1
    hours_worked_per_day = 10 # works 10 hours a day
    hours_per_task = 2 # each task takes him two hours to complete
    tasks_per_day = hours_worked_per_day / hours_per_task

    # L2
    payment_per_task = 40 # pays him $40 per task
    earnings_per_day = payment_per_task * tasks_per_day

    # L3
    days_in_a_week = 7 # a whole week
    total_earnings_per_week = earnings_per_day * days_in_a_week

    # FA
    answer = total_earnings_per_week
    return answer