def solve():
    """Index: 1967.
    Returns: the total number of hot dogs Guise had eaten by Wednesday that week.
    """
    # L1
    hot_dogs_monday = 10 # ten hot dogs on a Monday
    daily_increase = 2 # two more dogs each day than the previous day
    hot_dogs_tuesday = hot_dogs_monday + daily_increase

    # L2
    total_by_tuesday = hot_dogs_tuesday + hot_dogs_monday

    # L3
    hot_dogs_wednesday = hot_dogs_tuesday + daily_increase

    # L4
    total_by_wednesday = hot_dogs_wednesday + total_by_tuesday

    # FA
    answer = total_by_wednesday
    return answer