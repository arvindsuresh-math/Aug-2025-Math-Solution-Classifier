def solve():
    """Index: 249.
    Returns: the number of dandelion puffs each friend received.
    """
    # L1
    original_puffs = 40 # he originally picked 40 dandelion puffs
    mom_puffs = 3 # gave 3 to his mom
    sister_puffs = 3 # another 3 to his sister
    grandmother_puffs = 5 # 5 to his grandmother
    dog_puffs = 2 # 2 to his dog
    remaining_puffs = original_puffs - mom_puffs - sister_puffs - grandmother_puffs - dog_puffs

    # L2
    num_friends = 3 # his 3 friends
    puffs_per_friend = remaining_puffs / num_friends

    # FA
    answer = puffs_per_friend
    return answer