def solve():
    """Index: 589.
    Returns: the number of square tables needed so that 90 pupils can read at the same time.
    """
    # L1
    num_rectangular_tables = 7 # 7 rectangular tables
    seats_per_rectangular_table = 10 # A rectangular table seats 10 pupils
    rectangular_seats = num_rectangular_tables * seats_per_rectangular_table

    # L2
    total_pupils = 90 # 90 pupils can read at the same time
    square_table_seats_needed = total_pupils - rectangular_seats

    # L3
    seats_per_square_table = 4 # a square table seats 4 pupils
    num_square_tables = square_table_seats_needed / seats_per_square_table

    # FA
    answer = num_square_tables
    return answer