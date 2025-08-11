def solve():
    """Index: 6113.
    Returns: the total number of chairs Jackson needs to buy.
    """
    # L1
    chairs_per_four_seat_table = 4 # 4 seats
    num_four_seat_tables = 6 # 6 tables with 4 seats
    chairs_for_four_seat_tables = chairs_per_four_seat_table * num_four_seat_tables

    # L2
    chairs_per_six_seat_table = 6 # 6 seats
    num_six_seat_tables = 12 # 12 tables with 6 seats
    chairs_for_six_seat_tables = chairs_per_six_seat_table * num_six_seat_tables

    # L3
    total_chairs = chairs_for_four_seat_tables + chairs_for_six_seat_tables

    # FA
    answer = total_chairs
    return answer