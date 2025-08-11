def solve():
    """Index: 951.
    Returns: the total number of people going to Michonne’s birthday party.
    """
    # L1
    school_friends = 6 # 6 of her friends from school
    neighborhood_friends = 12 # 12 of her friends from her neighborhood
    total_friends = school_friends + neighborhood_friends

    # L2
    friends_brought = 2 # bring two friends along as well
    additional_guests = total_friends * friends_brought

    # L3
    total_people = total_friends + additional_guests

    # FA
    answer = total_people
    return answer