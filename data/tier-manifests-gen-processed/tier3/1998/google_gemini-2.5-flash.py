def solve():
    """Index: 1998.
    Returns: the number of marbles each friend received.
    """
    # L1
    total_marbles = 100 # Harold had 100 marbles
    marbles_kept = 20 # He kept 20 marbles
    marbles_shared = total_marbles - marbles_kept

    # L2
    num_friends = 5 # among his 5 friends
    marbles_per_friend = marbles_shared / num_friends

    # FA
    answer = marbles_per_friend
    return answer