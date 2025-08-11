def solve():
    """Index: 2274.
    Returns: the number of friends James has left.
    """
    # L1
    initial_friends = 20 # James has 20 friends
    lost_friends = 2 # got into an argument with 2 of his friends
    friends_after_loss = initial_friends - lost_friends

    # L2
    new_friends = 1 # he made one more friend
    total_friends = friends_after_loss + new_friends

    # FA
    answer = total_friends
    return answer