def solve():
    """Index: 1200.
    Returns: the total time Kitty spent cleaning the living room after a certain number of weeks.
    """
    # L1
    pickup_toys_minutes = 5 # 5 minutes to pick up toys
    vacuum_minutes = 20 # 20 minutes to vacuum the living room floor
    windows_minutes = 15 # 15 minutes cleaning the windows
    dusting_minutes = 10 # 10 minutes dusting the furniture
    total_minutes_per_week = pickup_toys_minutes + vacuum_minutes + windows_minutes + dusting_minutes

    # L2
    num_weeks = 4 # After 4 weeks
    total_cleaning_time = num_weeks * total_minutes_per_week

    # FA
    answer = total_cleaning_time
    return answer