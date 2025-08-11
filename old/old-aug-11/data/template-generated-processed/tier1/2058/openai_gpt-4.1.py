def solve():
    """Index: 2058.
    Returns: the total number of points Tobee, Jay, and Sean scored for their team.
    """
    # L1
    tobee_points = 4 # Tobee scored 4 points
    jay_more_than_tobee = 6 # Jay scored 6 more than Tobee
    jay_points = tobee_points + jay_more_than_tobee

    # L2
    tobee_jay_total = tobee_points + jay_points

    # L3
    sean_less_than_tobee_jay = 2 # Sean scored 2 less than the points of Tobee and Jay together
    sean_points = tobee_jay_total - sean_less_than_tobee_jay

    # L4
    total_points = tobee_points + jay_points + sean_points

    # FA
    answer = total_points
    return answer