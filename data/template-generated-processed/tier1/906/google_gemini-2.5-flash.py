def solve():
    """Index: 906.
    Returns: the number of passengers on the bus after the third stop.
    """
    # L1
    first_stop_on = 7 # 7 people got on
    passengers_after_first_stop = first_stop_on

    # L2
    second_stop_off = 3 # 3 people got off
    second_stop_on = 5 # 5 people got on
    passengers_after_second_stop = passengers_after_first_stop + second_stop_on - second_stop_off

    # L3
    third_stop_off = 2 # 2 people got off
    third_stop_on = 4 # 4 people got on
    passengers_after_third_stop = passengers_after_second_stop + third_stop_on - third_stop_off

    # FA
    answer = passengers_after_third_stop
    return answer