def solve():
    """Index: 651.
    Returns: the total money Olivia made this week.
    """
    # L1
    hourly_rate = 9 # $9 per hour
    hours_monday = 4 # 4 hours on Monday
    earnings_monday = hourly_rate * hours_monday

    # L2
    hours_wednesday = 3 # 3 hours on Wednesday
    earnings_wednesday = hourly_rate * hours_wednesday

    # L3
    hours_friday = 6 # 6 hours on Friday
    earnings_friday = hourly_rate * hours_friday

    # L4
    total_earnings_week = earnings_monday + earnings_wednesday + earnings_friday

    # FA
    answer = total_earnings_week
    return answer