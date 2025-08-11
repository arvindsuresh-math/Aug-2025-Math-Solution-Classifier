def solve():
    """Index: 3498.
    Returns: the total amount of money each of Harry's friends contributed.
    """
    # L1
    harry_contribution = 30 # Harry added $30
    total_multiplier = 3 # three times as much as Harry contributed
    total_contribution = total_multiplier * harry_contribution

    # L2
    friends_total_contribution = total_contribution - harry_contribution

    # L3
    num_friends = 3 # His three friends decided to contribute
    each_friend_contribution = friends_total_contribution / num_friends

    # FA
    answer = each_friend_contribution
    return answer