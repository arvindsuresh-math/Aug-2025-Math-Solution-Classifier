def solve():
    """Index: 1908.
    Returns: the total number of pets Taylor and his friends have together.
    """
    # L1
    taylor_pets = 4 # Taylor has 4 pets
    multiplier_first_friends = 2 # each having twice as many pets as Taylor has
    pets_per_first_friend = taylor_pets * multiplier_first_friends

    # L2
    num_first_friends = 3 # 3 of his friends come first
    total_pets_first_friends = pets_per_first_friend * num_first_friends

    # L3
    num_other_friends = 2 # another two of his friends
    pets_per_other_friend = 2 # 2 pets each
    total_pets_other_friends = num_other_friends * pets_per_other_friend

    # L4
    total_pets = taylor_pets + total_pets_other_friends + total_pets_first_friends

    # FA
    answer = total_pets
    return answer