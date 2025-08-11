def solve():
    """Index: 2779.
    Returns: the total number of points Olaf and his dad scored.
    """
    # L1
    dad_points = 7 # dad, who scored 7 points
    olaf_multiplier = 3 # three times more points than his dad
    olaf_points = dad_points * olaf_multiplier

    # L2
    total_points = olaf_points + dad_points

    # FA
    answer = total_points
    return answer