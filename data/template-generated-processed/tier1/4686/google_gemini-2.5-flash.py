def solve():
    """Index: 4686.
    Returns: the number of remaining pieces of clothing Darcy has to fold.
    """
    # L1
    total_shirts = 20 # 20 shirts
    folded_shirts = 12 # folds 12 of the shirts
    remaining_shirts = total_shirts - folded_shirts

    # L2
    total_shorts = 8 # 8 pairs of shorts
    folded_shorts = 5 # 5 of the shorts
    remaining_shorts = total_shorts - folded_shorts

    # L3
    total_remaining_to_fold = remaining_shirts + remaining_shorts

    # FA
    answer = total_remaining_to_fold
    return answer