def solve():
    """Index: 5090.
    Returns: the total number of votes Mark got.
    """
    # L1
    total_voters = 100000 # 100,000 voters
    win_percent_decimal = 0.7 # wins 70% of the votes
    votes_first_area = total_voters * win_percent_decimal

    # L2
    multiplier_remaining_area = 2 # twice as many total votes
    votes_remaining_area = votes_first_area * multiplier_remaining_area

    # L3
    total_votes = votes_remaining_area + votes_first_area

    # FA
    answer = total_votes
    return answer