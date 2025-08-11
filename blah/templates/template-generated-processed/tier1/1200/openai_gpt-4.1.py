def solve():
    """Index: 1200.
    Returns: the total number of minutes Kitty spent cleaning the living room after 4 weeks.
    """
    # L1
    pickup_minutes = 5 # 5 minutes to pick up toys
    vacuum_minutes = 20 # 20 minutes to vacuum
    windows_minutes = 15 # 15 minutes cleaning the windows
    furniture_minutes = 10 # 10 minutes dusting the furniture
    total_per_week = pickup_minutes + vacuum_minutes + windows_minutes + furniture_minutes

    # L2
    num_weeks = 4 # After 4 weeks
    total_minutes = num_weeks * total_per_week

    # FA
    answer = total_minutes
    return answer