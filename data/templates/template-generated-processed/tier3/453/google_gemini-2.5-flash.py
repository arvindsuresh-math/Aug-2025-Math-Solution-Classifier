def solve():
    """Index: 453.
    Returns: the number of shells each friend received.
    """
    # L1
    jillian_shells = 29 # Jillian collected 29
    savannah_shells = 17 # Savannah collected 17
    clayton_shells = 8 # Clayton collected 8
    total_shells_collected = jillian_shells + savannah_shells + clayton_shells

    # L2
    num_friends = 2 # two of their friends
    shells_per_friend = total_shells_collected / num_friends

    # FA
    answer = shells_per_friend
    return answer