def solve():
    """Index: 3443.
    Returns: the amount Hannah gets paid this week.
    """
    # L1
    hours_worked_per_week = 18 # works 18 hours per week
    hourly_rate = 30 # makes $30/hour
    total_earnings_before_dock = hours_worked_per_week * hourly_rate

    # L2
    times_late = 3 # late 3 times this week
    dock_per_late = 5 # docked $5 each time
    total_docked_amount = times_late * dock_per_late

    # L3
    final_pay = total_earnings_before_dock - total_docked_amount

    # FA
    answer = final_pay
    return answer