def solve():
    """Index: 6487.
    Returns: the initial number of marbles Zack had.
    """
    # L1
    num_friends = 3 # three friends
    marbles_per_friend = 20 # 20 marbles each
    marbles_given_to_friends = num_friends * marbles_per_friend

    # L2
    marbles_kept = 5 # kept five
    initial_marbles = marbles_given_to_friends + marbles_kept

    # FA
    answer = initial_marbles
    return answer