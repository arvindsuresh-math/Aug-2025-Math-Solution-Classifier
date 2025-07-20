def solve():
    """Index: 6603.
    Returns: the number of seats that will not be occupied on the plane.
    """
    # L1
    people_per_row = 8 # Eight people fit in a row
    num_rows = 12 # 12 rows
    total_seats = people_per_row * num_rows

    # L2
    allowed_fraction_numerator = 3 # 3/4 of the seats
    allowed_fraction_denominator = 4 # 3/4 of the seats
    allowed_seats_per_row = people_per_row * allowed_fraction_numerator / allowed_fraction_denominator

    # L3
    total_allowed_seats = allowed_seats_per_row * num_rows

    # L4
    unoccupied_seats = total_seats - total_allowed_seats

    # FA
    answer = unoccupied_seats
    return answer