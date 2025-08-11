def solve():
    """Index: 1967.
    Returns: the total number of hot dogs Guise ate by Wednesday.
    """
    # L1
    monday_hot_dogs = 10 # ate ten hot dogs on a Monday
    daily_increase = 2 # ate two more dogs each day than the previous day
    tuesday_hot_dogs = monday_hot_dogs + daily_increase

    # L2
    tuesday_total = tuesday_hot_dogs + monday_hot_dogs

    # L3
    wednesday_hot_dogs = tuesday_hot_dogs + daily_increase

    # L4
    total_by_wednesday = wednesday_hot_dogs + tuesday_total

    # FA
    answer = total_by_wednesday
    return answer