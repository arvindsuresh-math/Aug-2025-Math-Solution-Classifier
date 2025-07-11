def solve():
    """Index: 477.
    Returns: the number of friends who attended the reception.
    """
    # L1
    bride_invited_couples = 20 # invited 20 couples from their side of the family
    guests_per_couple = 2 # WK
    bride_guests = bride_invited_couples * guests_per_couple

    # L2
    groom_invited_couples = 20 # invited 20 couples from their side of the family
    groom_guests = groom_invited_couples * guests_per_couple

    # L3
    total_people = 180 # 180 people
    friends_attended = total_people - (bride_guests + groom_guests)

    # FA
    answer = friends_attended
    return answer