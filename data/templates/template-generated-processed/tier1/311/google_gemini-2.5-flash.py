def solve():
    """Index: 311.
    Returns: the number of empty seats on the bus after the second stop.
    """
    # L1
    num_rows = 23 # 23 rows
    seats_per_row = 4 # 4 seats
    total_seats = num_rows * seats_per_row

    # L2
    initial_people = 16 # 16 people climb
    board_first_stop = 15 # 15 people board the bus
    get_off_first_stop = 3 # 3 get off
    people_after_first_stop = initial_people + board_first_stop - get_off_first_stop

    # L3
    board_second_stop = 17 # 17 people get on the bus
    get_off_second_stop = 10 # 10 get off
    people_after_second_stop = people_after_first_stop + board_second_stop - get_off_second_stop

    # L4
    empty_seats = total_seats - people_after_second_stop

    # FA
    answer = empty_seats
    return answer