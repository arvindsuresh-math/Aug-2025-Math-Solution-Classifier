def solve():
    """Index: 1280.
    Returns: the total amount Honey saved in 20 days.
    """
    # L1
    days_worked = 20 # After 20 days of work
    daily_earnings = 80 # earned $80 a day
    total_earned = days_worked * daily_earnings

    # L2
    total_spent = 1360 # she spent $1360
    total_saved = total_earned - total_spent

    # FA
    answer = total_saved
    return answer