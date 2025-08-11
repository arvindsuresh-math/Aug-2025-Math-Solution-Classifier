def solve():
    """Index: 235.
    Returns: the total number of trains Max has.
    """
    # L1
    trains_per_birthday = 1 # one for every birthday
    trains_per_christmas = 2 # two each Christmas
    trains_per_year = trains_per_birthday + trains_per_christmas

    # L2
    num_years = 5 # 5 years
    trains_after_years = num_years * trains_per_year

    # L3
    multiplier_double = 2 # double the number of trains
    trains_doubled_by_parents = trains_after_years * multiplier_double

    # L4
    total_trains = trains_after_years + trains_doubled_by_parents

    # FA
    answer = total_trains
    return answer