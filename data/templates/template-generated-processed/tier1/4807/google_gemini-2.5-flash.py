def solve():
    """Index: 4807.
    Returns: the difference in points between Cole and Freddy's team and Brayden and Gavin's team.
    """
    # L1
    brayden_gavin_touchdowns = 7 # Brayden and Gavin scored 7 touchdowns
    points_per_touchdown = 7 # Touchdowns were worth 7 points
    brayden_gavin_points = brayden_gavin_touchdowns * points_per_touchdown

    # L2
    cole_freddy_touchdowns = 9 # Cole and Freddy's team scored 9 touchdowns
    cole_freddy_points = cole_freddy_touchdowns * points_per_touchdown

    # L3
    point_difference = cole_freddy_points - brayden_gavin_points

    # FA
    answer = point_difference
    return answer