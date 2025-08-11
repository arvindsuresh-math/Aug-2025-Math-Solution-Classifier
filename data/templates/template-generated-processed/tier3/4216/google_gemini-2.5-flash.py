def solve():
    """Index: 4216.
    Returns: the total points earned by the Golden State Team.
    """
    # L1
    draymond_points = 12 # Draymond earned 12 points
    curry_multiplier = 2 # twice the points as Draymond
    curry_points = draymond_points * curry_multiplier

    # L2
    kelly_points = 9 # Kelly earned 9
    durant_multiplier = 2 # twice the points as Kelly
    durant_points = kelly_points * durant_multiplier

    # L3
    klay_divisor = 2 # half the points as Draymond
    klay_points = draymond_points / klay_divisor

    # L4
    total_points = draymond_points + curry_points + kelly_points + durant_points + klay_points

    # FA
    answer = total_points
    return answer