def solve():
    """Index: 4479.
    Returns: the number of ears of corn Bob has left.
    """
    # L1
    stacy_ears_taken = 21 # 21 ears of corn
    ears_per_bushel = 14 # 14 ears of corn
    stacy_bushels_taken = stacy_ears_taken / ears_per_bushel

    # L2
    terry_bushels = 8 # 8 bushels
    jerry_bushels = 3 # 3
    linda_bushels = 12 # 12 bushels
    total_bushels_given_away = terry_bushels + jerry_bushels + linda_bushels + stacy_bushels_taken

    # L3
    initial_bushels = 50 # 50 bushels
    remaining_bushels = initial_bushels - total_bushels_given_away

    # L4
    remaining_ears = remaining_bushels * ears_per_bushel

    # FA
    answer = remaining_ears
    return answer