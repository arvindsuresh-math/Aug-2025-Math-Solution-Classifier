def solve():
    """Index: 993.
    Returns: the number of cards Rick gave to Miguel.
    """
    # L1
    total_cards_initial = 130 # Rick has 130 cards
    cards_kept = 15 # only keep 15 cards
    cards_after_keeping = total_cards_initial - cards_kept

    # L2
    num_friends = 8 # saw 8 friends
    cards_per_friend = 12 # give them 12 cards each
    cards_given_to_friends = num_friends * cards_per_friend

    # L3
    num_sisters = 2 # his 2 sisters
    cards_per_sister = 3 # each of Rick's sisters got 3 cards
    cards_given_to_sisters = num_sisters * cards_per_sister

    # L4
    cards_given_to_others = cards_given_to_friends + cards_given_to_sisters

    # L5
    cards_given_to_miguel = cards_after_keeping - cards_given_to_others

    # FA
    answer = cards_given_to_miguel
    return answer