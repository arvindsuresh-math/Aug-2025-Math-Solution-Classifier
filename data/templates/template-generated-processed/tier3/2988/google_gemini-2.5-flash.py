def solve():
    """Index: 2988.
    Returns: the total time Hadassah took to finish all the paintings.
    """
    # L1
    hours_initial = 6 # six hours
    paintings_initial = 12 # 12 paintings
    paintings_per_hour = paintings_initial / hours_initial

    # L2
    additional_paintings = 20 # 20 more paintings
    time_for_additional_paintings = additional_paintings / paintings_per_hour

    # L3
    total_time = time_for_additional_paintings + hours_initial

    # FA
    answer = total_time
    return answer