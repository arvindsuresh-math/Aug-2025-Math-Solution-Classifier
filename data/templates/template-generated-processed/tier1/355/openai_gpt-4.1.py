def solve():
    """Index: 355.
    Returns: the number of squares Marla colors green.
    """
    # L1
    num_rows = 10 # 10 rows
    squares_per_row = 15 # 15 squares in each row
    total_squares = num_rows * squares_per_row

    # L2
    red_rows = 4 # 4 rows
    red_squares_per_row = 6 # 6 squares in the middle
    red_squares = red_rows * red_squares_per_row

    # L3
    blue_rows_top = 2 # first 2 rows
    blue_rows_bottom = 2 # last 2 rows
    total_blue_rows = blue_rows_top + blue_rows_bottom

    # L4
    blue_squares = total_blue_rows * squares_per_row

    # L5
    red_or_blue_squares = red_squares + blue_squares

    # L6
    green_squares = total_squares - red_or_blue_squares

    # FA
    answer = green_squares
    return answer