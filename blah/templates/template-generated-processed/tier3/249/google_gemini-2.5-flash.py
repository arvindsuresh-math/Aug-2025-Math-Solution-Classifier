def solve():
    """Index: 249.
    Returns: the number of dandelion puffs each friend received.
    """
    # L1
    original_puffs = 40 # he originally picked 40 dandelion puffs
    given_to_mom = 3 # He gave 3 to his mom
    given_to_sister = 3 # another 3 to his sister
    given_to_grandmother = 5 # 5 to his grandmother
    given_to_dog = 2 # and 2 to his dog
    remaining_puffs = original_puffs - given_to_mom - given_to_sister - given_to_grandmother - given_to_dog

    # L2
    num_friends = 3 # divided the remaining dandelion puffs equally among his 3 friends
    puffs_per_friend = remaining_puffs / num_friends

    # FA
    answer = puffs_per_friend
    return answer