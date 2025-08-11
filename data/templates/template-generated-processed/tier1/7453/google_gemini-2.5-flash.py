def solve():
    """Index: 7453.
    Returns: the number of people on the combined list after removing duplicates.
    """
    # L1
    james_friends = 75 # James has 75 friends
    john_multiplier = 3 # John has 3 times as many friends as James
    john_friends = james_friends * john_multiplier

    # L2
    total_friends_before_duplicates = john_friends + james_friends

    # L3
    shared_friends = 25 # They share 25 friends
    combined_list_unique = total_friends_before_duplicates - shared_friends

    # FA
    answer = combined_list_unique
    return answer