def solve():
    """Index: 4898.
    Returns: the total number of wheels at the train station.
    """
    # L1
    rows_per_carriage = 3 # 3 rows of wheels
    wheels_per_row = 5 # 5 wheels each
    wheels_per_carriage = rows_per_carriage * wheels_per_row

    # L2
    carriages_per_train = 4 # each train has 4 carriages
    wheels_per_train = carriages_per_train * wheels_per_carriage

    # L3
    num_trains = 4 # 4 trains waiting
    total_wheels = num_trains * wheels_per_train

    # FA
    answer = total_wheels
    return answer