def solve():
    """Index: 1158.
    Returns: the total number of bags James delivers in 5 days.
    """
    # L1
    bags_per_trip = 10 # 10 bags on each trip
    trips_per_day = 20 # 20 trips a day
    bags_per_day = bags_per_trip * trips_per_day

    # L2
    num_days = 5 # in 5 days
    total_bags = bags_per_day * num_days

    # FA
    answer = total_bags
    return answer