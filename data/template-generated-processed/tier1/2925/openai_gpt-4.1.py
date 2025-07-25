def solve():
    """Index: 2925.
    Returns: the number of seats that were taken at the school play.
    """
    # L1
    num_rows = 40 # 40 rows of chairs
    chairs_per_row = 20 # 20 chairs in each row
    total_chairs = num_rows * chairs_per_row

    # L2
    unoccupied_seats = 10 # only 10 seats were not occupied
    seats_taken = total_chairs - unoccupied_seats

    # FA
    answer = seats_taken
    return answer