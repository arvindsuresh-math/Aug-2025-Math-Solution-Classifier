def solve():
    """Index: 235.
    Returns: the total number of model trains Max has after 5 years and the doubling gift.
    """
    # L1
    trains_per_birthday = 1 # one for every birthday
    trains_per_christmas = 2 # two each Christmas
    trains_per_year = trains_per_birthday + trains_per_christmas

    # L2
    years = 5 # every year for 5 years
    total_trains_before_double = years * trains_per_year

    # L3
    double_multiplier = 2 # double the number of trains
    doubled_trains = total_trains_before_double * double_multiplier

    # L4
    total_trains = total_trains_before_double + doubled_trains

    # FA
    answer = total_trains
    return answer