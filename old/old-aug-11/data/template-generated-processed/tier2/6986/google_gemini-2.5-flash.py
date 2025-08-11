def solve():
    """Index: 6986.
    Returns: the total amount of money the cab rides cost would be at the end of the event.
    """
    # L1
    distance_one_way = 200 # event is 200 miles away
    cost_per_mile = 2.5 # cab ride costs $2.5 per mile
    cost_one_way = distance_one_way * cost_per_mile

    # L2
    cost_per_day = cost_one_way + cost_one_way

    # L3
    days_per_week = 7 # WK
    total_cab_cost = cost_per_day * days_per_week

    # FA
    answer = total_cab_cost
    return answer