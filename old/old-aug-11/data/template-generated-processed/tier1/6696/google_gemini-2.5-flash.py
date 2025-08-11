def solve():
    """Index: 6696.
    Returns: the total pounds of sugar Jack will have in the end.
    """
    # L1
    initial_sugar = 65 # Jack has 65 pounds of sugar today
    sugar_used_tomorrow = 18 # he will use 18 pounds of sugar
    sugar_tomorrow = initial_sugar - sugar_used_tomorrow

    # L2
    sugar_bought_following_day = 50 # he will buy 50 more pounds of sugar
    sugar_end = sugar_tomorrow + sugar_bought_following_day

    # FA
    answer = sugar_end
    return answer