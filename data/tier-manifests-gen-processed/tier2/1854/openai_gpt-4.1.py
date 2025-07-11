def solve():
    """Index: 1854.
    Returns: the number of individual corn cobs Clyde picked.
    """
    # L1
    num_bushels = 2 # picked 2 bushels of corn
    bushel_weight = 56 # each bushel weighs 56 pounds
    total_corn_weight = num_bushels * bushel_weight

    # L2
    ear_weight = 0.5 # each ear of corn weighs .5 pounds
    num_ears = total_corn_weight / ear_weight

    # FA
    answer = num_ears
    return answer