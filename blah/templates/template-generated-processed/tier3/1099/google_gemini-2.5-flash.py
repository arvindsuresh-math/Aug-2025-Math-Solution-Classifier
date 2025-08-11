def solve():
    """Index: 1099.
    Returns: the number of hours the stand needs to run.
    """
    # L1
    price_per_hotdog = 2 # each one selling for $2
    hotdogs_per_hour = 10 # sells 10 hot dogs every hour
    sales_per_hour = price_per_hotdog * hotdogs_per_hour

    # L2
    sales_goal = 200 # make $200 in sales
    hours_needed = sales_goal / sales_per_hour

    # FA
    answer = hours_needed
    return answer