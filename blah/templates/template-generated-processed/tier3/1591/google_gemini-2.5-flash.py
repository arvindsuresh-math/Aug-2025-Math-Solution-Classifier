def solve():
    """Index: 1591.
    Returns: the number of balloons one school will receive.
    """
    # L1
    yellow_balloons = 3414 # 3414 yellow balloons
    more_black_balloons = 1762 # 1762 more black balloons than yellow balloons
    black_balloons = yellow_balloons + more_black_balloons

    # L2
    total_balloons = yellow_balloons + black_balloons

    # L3
    num_schools = 10 # evenly divided among 10 schools
    balloons_per_school = total_balloons / num_schools

    # FA
    answer = balloons_per_school
    return answer