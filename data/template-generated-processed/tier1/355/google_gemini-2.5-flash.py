def solve():
    """Index: 355.
    Returns: the number of squares Marla colors green.
    """
    # L1
    num_rows = 10 # 10 rows
    squares_per_row = 15 # 15 squares in each row
    total_squares_grid = num_rows * squares_per_row

    # L2
    red_rows = 4 # 4 rows of 6 squares
    red_squares_per_row = 6 # 6 squares in the middle of the grid with red
    red_squares = red_rows * red_squares_per_row

    # L3
    first_blue_rows = 2 # first 2 and last 2 rows
    last_blue_rows = 2 # first 2 and last 2 rows
    total_blue_rows = first_blue_rows + last_blue_rows

    # L4
    blue_squares = total_blue_rows * squares_per_row

    # L5
    red_or_blue_squares = red_squares + blue_squares

    # L6
    green_squares = total_squares_grid - red_or_blue_squares

    # FA
    answer = green_squares
    return answer