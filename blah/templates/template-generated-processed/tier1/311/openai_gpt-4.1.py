def solve():
    """Index: 311.
    Returns: the number of empty seats on the bus after the second stop.
    """
    # L1
    num_rows = 23 # 23 rows of 4 seats
    seats_per_row = 4 # 4 seats per row
    total_seats = num_rows * seats_per_row

    # L2
    initial_boarded = 16 # 16 people climb
    first_stop_boarded = 15 # 15 people board the bus
    first_stop_got_off = 3 # 3 get off
    people_after_first = initial_boarded + first_stop_boarded - first_stop_got_off

    # L3
    second_stop_boarded = 17 # 17 people get on the bus
    second_stop_got_off = 10 # 10 get off
    people_after_second = people_after_first + second_stop_boarded - second_stop_got_off

    # L4
    empty_seats = total_seats - people_after_second

    # FA
    answer = empty_seats
    return answer