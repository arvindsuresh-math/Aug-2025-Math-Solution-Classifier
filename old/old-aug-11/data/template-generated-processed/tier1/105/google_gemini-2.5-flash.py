def solve():
    """Index: 105.
    Returns: the total number of goats they have.
    """
    # L1
    washington_goats = 140 # Washington has 140 goats
    paddington_more_than_washington = 40 # Paddington has 40 more goats than Washington
    paddington_goats = washington_goats + paddington_more_than_washington

    # L2
    total_goats = washington_goats + paddington_goats

    # FA
    answer = total_goats
    return answer