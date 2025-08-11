def solve():
    """Index: 7310.
    Returns: the total number of chairs altogether.
    """
    # L1
    num_rows = 7 # 7 rows
    chairs_per_row = 12 # 12 chairs in each row
    initial_chairs = num_rows * chairs_per_row

    # L2
    extra_chairs = 11 # 11 extra chairs
    total_chairs = initial_chairs + extra_chairs

    # FA
    answer = total_chairs
    return answer