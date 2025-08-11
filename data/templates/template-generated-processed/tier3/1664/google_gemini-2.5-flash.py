def solve():
    """Index: 1664.
    Returns: the total number of matches Brendan won.
    """
    # L1
    first_rounds = 2 # first 2 rounds
    matches_per_round = 6 # each of which had 6 matches
    matches_won_first_rounds = first_rounds * matches_per_round

    # L2
    matches_last_round = 4 # 4 matches in the last round
    half_divisor = 2 # wins half of the 4 matches
    matches_won_last_round = matches_last_round / half_divisor

    # L3
    total_matches_won = matches_won_first_rounds + matches_won_last_round

    # FA
    answer = total_matches_won
    return answer