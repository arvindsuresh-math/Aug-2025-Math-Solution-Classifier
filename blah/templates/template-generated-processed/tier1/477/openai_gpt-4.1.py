def solve():
    """Index: 477.
    Returns: the number of friends who attended the wedding reception.
    """
    # L1
    bride_couples = 20 # bride invited 20 couples
    guests_per_couple = 2 # WK (2 guests/couple)
    bride_guests = bride_couples * guests_per_couple

    # L2
    groom_couples = 20 # groom invited 20 couples
    groom_guests = groom_couples * guests_per_couple

    # L3
    total_guests = 180 # wedding reception had 180 people
    friends = total_guests - (bride_guests + groom_guests)

    # FA
    answer = friends
    return answer