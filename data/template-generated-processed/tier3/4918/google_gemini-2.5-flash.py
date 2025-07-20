def solve():
    """Index: 4918.
    Returns: the total points scored by the team.
    """
    # L1
    bailey_points = 14 # If Bailey scored 14 points
    michiko_divisor = 2 # half as many points as did Bailey
    michiko_points = bailey_points / michiko_divisor

    # L2
    akiko_more_points = 4 # Akiko scored 4 more points
    akiko_points = michiko_points + akiko_more_points

    # L3
    chandra_multiplier = 2 # Chandra scored twice as many points
    chandra_points = akiko_points * chandra_multiplier

    # L4
    total_team_points = bailey_points + michiko_points + akiko_points + chandra_points

    # FA
    answer = total_team_points
    return answer