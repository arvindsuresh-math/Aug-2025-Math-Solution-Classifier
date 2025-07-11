def solve():
    """Index: 2171.
    Returns: how many more points the first team scored than the second team.
    """
    # L1
    beth_score = 12 # Beth scored 12
    jan_score = 10 # Jan scored 10
    first_team_total = beth_score + jan_score

    # L2
    judy_score = 8 # Judy scored 8
    angel_score = 11 # Angel scored 11
    second_team_total = judy_score + angel_score

    # L3
    difference = first_team_total - second_team_total

    # FA
    answer = difference
    return answer