def solve():
    """Index: 1329.
    Returns: the difference in votes between the third candidate and John.
    """
    # L1
    total_voters = 1150 # 1150 people voting
    john_votes = 150 # John manages to capture 150 votes
    remaining_votes = total_voters - john_votes

    # L2
    james_vote_percent = 0.7 # 70% of the remaining vote
    james_votes = remaining_votes * james_vote_percent

    # L3
    third_guy_votes = remaining_votes - james_votes

    # L4
    vote_difference = third_guy_votes - john_votes

    # FA
    answer = vote_difference
    return answer