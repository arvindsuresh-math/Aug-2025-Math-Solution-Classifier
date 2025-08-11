def solve():
    """Index: 205.
    Returns: the total number of plates Wickham needs.
    """
    # L1
    initial_guests = 30 # He invites 30 people
    plus_one_divisor = 2 # half of the guests
    guests_with_plus_one = initial_guests / plus_one_divisor

    # L2
    total_guests = initial_guests + guests_with_plus_one

    # L3
    num_courses = 3 # a 3-course meal
    total_plates_needed = total_guests * num_courses

    # FA
    answer = total_plates_needed
    return answer