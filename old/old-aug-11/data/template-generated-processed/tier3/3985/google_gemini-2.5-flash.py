def solve():
    """Index: 3985.
    Returns: the average points scored per player on the team.
    """
    # L1
    lefty_score = 20 # Lefty scores 20 points
    half_divisor = 2 # half as many as Lefty does
    righty_score = lefty_score / half_divisor

    # L2
    multiplier = 6 # 6 times as much as Righty does
    other_teammate_score = righty_score * multiplier

    # L3
    total_points = lefty_score + righty_score + other_teammate_score

    # L4
    num_players = 3 # three teammates
    average_points = total_points / num_players

    # FA
    answer = average_points
    return answer