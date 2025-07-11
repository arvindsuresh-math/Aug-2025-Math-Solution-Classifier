def solve():
    """Index: 382.
    Returns: the total number of minutes it will take David to wash all windows.
    """
    # L1
    total_windows = 64 # David's house has 64 windows
    windows_per_unit = 4 # wash 4 windows
    number_of_units = total_windows / windows_per_unit

    # L2
    minutes_per_unit = 10 # It takes David 10 minutes
    total_minutes = minutes_per_unit * number_of_units

    # FA
    answer = total_minutes
    return answer