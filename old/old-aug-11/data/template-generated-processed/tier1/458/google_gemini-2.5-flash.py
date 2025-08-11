def solve():
    """Index: 458.
    Returns: the number of votes Marcy got.
    """
    # L1
    joey_votes = 8 # Joey got 8 votes
    votes_more_than_joey = 3 # 3 more than the number of votes Joey got
    joey_plus_three = joey_votes + votes_more_than_joey

    # L2
    multiplier_for_barry = 2 # twice as many
    barry_votes = joey_plus_three * multiplier_for_barry

    # L3
    multiplier_for_marcy = 3 # three times as many votes
    marcy_votes = barry_votes * multiplier_for_marcy

    # FA
    answer = marcy_votes
    return answer