def solve():
    """Index: 458.
    Returns: the number of votes Marcy got.
    """
    # L1
    joey_votes = 8 # Joey got 8 votes
    add_to_joey = 3 # three to Joey's vote total
    joey_plus_three = joey_votes + add_to_joey

    # L2
    barry_multiplier = 2 # double that number
    barry_votes = joey_plus_three * barry_multiplier

    # L3
    marcy_multiplier = 3 # triple that number
    marcy_votes = barry_votes * marcy_multiplier

    # FA
    answer = marcy_votes
    return answer