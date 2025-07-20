def solve():
    """Index: 5496.
    Returns: the number of people currently on the trolley.
    """
    # L1
    initial_customers = 10 # 10 people on his 1st stop
    trolley_driver = 1 # trolley driver
    people_after_first_stop = trolley_driver + initial_customers

    # L2
    multiplier_twice = 2 # twice as many people
    people_on_second_stop = initial_customers * multiplier_twice

    # L3
    people_off_second_stop = 3 # 3 people got off
    people_after_second_stop = people_after_first_stop - people_off_second_stop + people_on_second_stop

    # L4
    people_off_third_stop = 18 # 18 people got off
    people_on_third_stop = 2 # 2 got on
    final_people_on_trolley = people_after_second_stop - people_off_third_stop + people_on_third_stop

    # FA
    answer = final_people_on_trolley
    return answer