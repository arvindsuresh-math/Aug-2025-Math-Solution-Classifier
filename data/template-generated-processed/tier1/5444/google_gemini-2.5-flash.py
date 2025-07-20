def solve():
    """Index: 5444.
    Returns: the total rainfall over the 3 days.
    """
    # L1
    monday_more_than_sunday = 3 # 3 inches more than Sunday
    sunday_rainfall = 4 # 4 inches on Sunday
    monday_rainfall = monday_more_than_sunday + sunday_rainfall

    # L2
    tuesday_multiplier = 2 # twice as much on Tuesday as Monday
    tuesday_rainfall = monday_rainfall * tuesday_multiplier

    # L3
    total_rainfall = monday_rainfall + tuesday_rainfall + sunday_rainfall

    # FA
    answer = total_rainfall
    return answer