def solve():
    """Index: 951.
    Returns: the total number of people going to Michonne's birthday party.
    """
    # L1
    friends_from_school = 6 # 6 of her friends from school
    friends_from_neighborhood = 12 # 12 of her friends from her neighborhood
    total_invited_friends = friends_from_school + friends_from_neighborhood

    # L2
    friends_bring_along_count = 2 # bring two friends along
    friends_brought_by_friends = total_invited_friends * friends_bring_along_count

    # L3
    total_people_at_party = total_invited_friends + friends_brought_by_friends

    # FA
    answer = total_people_at_party
    return answer