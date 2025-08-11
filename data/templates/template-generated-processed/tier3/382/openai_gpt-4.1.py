def solve():
    """Index: 382.
    Returns: the total number of minutes it will take David to wash all the windows.
    """
    # L1
    total_windows = 64 # David's house has 64 windows
    windows_per_unit = 4 # 4 windows per 10 minutes
    num_units = total_windows / windows_per_unit

    # L2
    minutes_per_unit = 10 # 10 minutes to wash 4 windows
    total_minutes = minutes_per_unit * num_units

    # FA
    answer = total_minutes
    return answer