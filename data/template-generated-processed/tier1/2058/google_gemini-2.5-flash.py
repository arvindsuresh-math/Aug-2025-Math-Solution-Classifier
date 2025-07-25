def solve():
    """Index: 2058.
    Returns: the total points scored by Tobee, Jay, and Sean for their team.
    """
    # L1
    tobee_score = 4 # Tobee scored 4 points
    jay_more_than_tobee = 6 # Jay scored 6 more than Tobee
    jay_score = tobee_score + jay_more_than_tobee

    # L2
    tobee_jay_total = tobee_score + jay_score

    # L3
    sean_less_than_tobee_jay = 2 # Sean scored 2 less than the points of Tobee and Jay together
    sean_score = tobee_jay_total - sean_less_than_tobee_jay

    # L4
    team_total_score = tobee_score + jay_score + sean_score

    # FA
    answer = team_total_score
    return answer