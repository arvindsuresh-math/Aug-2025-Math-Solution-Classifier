def solve():
    """Index: 4009.
    Returns: the total number of cards Jim gave away.
    """
    # L1
    brother_sets = 8 # 8 sets of cards to his brother
    cards_per_set = 13 # 1 set has 13 trading cards
    cards_to_brother = brother_sets * cards_per_set

    # L2
    sister_sets = 5 # 5 sets of cards to his sister
    cards_to_sister = sister_sets * cards_per_set

    # L3
    friend_sets = 2 # 2 sets of cards to his friend
    cards_to_friend = friend_sets * cards_per_set

    # L4
    total_cards_given_away = cards_to_brother + cards_to_sister + cards_to_friend

    # FA
    answer = total_cards_given_away
    return answer