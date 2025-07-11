def solve():
    """Index: 1329.
    Returns: how many more votes the third candidate got than John.
    """
    # L1
    total_voters = 1150 # 1150 people voting
    john_votes = 150 # John manages to capture 150 votes
    remaining_after_john = total_voters - john_votes

    # L2
    james_percent = 0.7 # James captures 70% of the remaining vote
    james_votes = remaining_after_john * james_percent

    # L3
    third_candidate_votes = remaining_after_john - james_votes

    # L4
    vote_difference = third_candidate_votes - john_votes

    # FA
    answer = vote_difference
    return answer