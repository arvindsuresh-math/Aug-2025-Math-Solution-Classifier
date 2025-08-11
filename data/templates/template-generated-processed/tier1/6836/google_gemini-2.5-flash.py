def solve():
    """Index: 6836.
    Returns: the total points scored by all three friends.
    """
    # L1
    darius_score = 10 # Darius scored 10 points
    marius_more_than_darius = 3 # 3 points more than Darius
    marius_score = darius_score + marius_more_than_darius

    # L2
    matt_more_than_darius = 5 # 5 points less than Matt (meaning Matt scored 5 more than Darius)
    matt_score = darius_score + matt_more_than_darius

    # L3
    total_score = marius_score + matt_score + darius_score

    # FA
    answer = total_score
    return answer