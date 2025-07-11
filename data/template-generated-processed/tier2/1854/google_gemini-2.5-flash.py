def solve():
    """Index: 1854.
    Returns: the total number of individual corn cobs picked.
    """
    # L1
    num_bushels = 2 # picked 2 bushels of corn
    pounds_per_bushel = 56 # weighs 56 pounds
    total_pounds_corn = num_bushels * pounds_per_bushel

    # L2
    weight_per_ear = 0.5 # weighs .5 pounds
    total_ears_corn = total_pounds_corn / weight_per_ear

    # FA
    answer = total_ears_corn
    return answer