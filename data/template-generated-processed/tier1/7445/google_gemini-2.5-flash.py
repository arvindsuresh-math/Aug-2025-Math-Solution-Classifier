def solve():
    """Index: 7445.
    Returns: the number of people on the bus after the third stop.
    """
    # L1
    initial_people_on_bus = 50 # 50 people on the city bus
    people_off_first_stop = 15 # 15 people got off
    people_after_first_stop = initial_people_on_bus - people_off_first_stop

    # L2
    people_off_second_stop = 8 # 8 people got off
    people_after_second_off = people_after_first_stop - people_off_second_stop

    # L3
    people_on_second_stop = 2 # 2 got on
    people_after_second_stop = people_after_second_off + people_on_second_stop

    # L4
    people_off_third_stop = 4 # 4 people got off
    people_after_third_off = people_after_second_stop - people_off_third_stop

    # L5
    people_on_third_stop = 3 # 3 people got on
    final_people_on_bus = people_after_third_off + people_on_third_stop

    # FA
    answer = final_people_on_bus
    return answer