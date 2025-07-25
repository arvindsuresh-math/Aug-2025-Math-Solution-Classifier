def solve():
    """Index: 5131.
    Returns: the total points of their team.
    """
    # L1
    connor_score = 2 # Connor scored 2 in a game
    amy_more_than_connor = 4 # Amy scored 4 more than Connor
    amy_score = connor_score + amy_more_than_connor

    # L2
    jason_multiplier = 2 # Jason scored twice the score of Amy
    jason_score = amy_score * jason_multiplier

    # L3
    team_score = connor_score + amy_score + jason_score

    # FA
    answer = team_score
    return answer