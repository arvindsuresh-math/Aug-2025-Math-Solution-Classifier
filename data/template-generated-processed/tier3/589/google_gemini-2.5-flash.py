def solve():
    """Index: 589.
    Returns: the number of square tables needed.
    """
    # L1
    num_rectangular_tables = 7 # 7 rectangular tables
    seats_per_rectangular_table = 10 # rectangular table seats 10 pupils
    pupils_at_rectangular_tables = num_rectangular_tables * seats_per_rectangular_table

    # L2
    total_pupils_needed = 90 # 90 pupils can read
    pupils_at_square_tables = total_pupils_needed - pupils_at_rectangular_tables

    # L3
    seats_per_square_table = 4 # square table seats 4 pupils
    num_square_tables = pupils_at_square_tables / seats_per_square_table

    # FA
    answer = num_square_tables
    return answer