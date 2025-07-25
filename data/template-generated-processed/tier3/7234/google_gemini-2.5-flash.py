def solve():
    """Index: 7234.
    Returns: the number of dominoes each player will receive.
    """
    # L1
    jean_count = 1 # Jean
    friends_count = 3 # her three friends
    total_players = jean_count + friends_count

    # L2
    total_dominoes = 28 # There are 28 dominoes in the set
    dominoes_per_player = total_dominoes / total_players

    # FA
    answer = dominoes_per_player
    return answer