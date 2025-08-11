def solve():
    """Index: 2274.
    Returns: the number of friends James has left.
    """
    # L1
    initial_friends = 20 # James has 20 friends
    friends_lost = 2 # got into an argument with 2 of his friends
    friends_after_loss = initial_friends - friends_lost

    # L2
    friends_gained = 1 # he made one more friend
    final_friends = friends_after_loss + friends_gained

    # FA
    answer = final_friends
    return answer