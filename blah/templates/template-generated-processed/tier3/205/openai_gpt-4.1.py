def solve():
    """Index: 205.
    Returns: the total number of plates needed for the guests.
    """
    # L1
    invited_guests = 30 # invites 30 people
    plus_one_divisor = 2 # half of the guests bring a plus one
    guests_with_plus_one = invited_guests / plus_one_divisor

    # L2
    total_guests = invited_guests + guests_with_plus_one

    # L3
    courses = 3 # 3-course meal
    total_plates = total_guests * courses

    # FA
    answer = total_plates
    return answer