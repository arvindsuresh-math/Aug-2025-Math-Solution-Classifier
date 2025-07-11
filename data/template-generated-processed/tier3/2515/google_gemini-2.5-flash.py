def solve():
    """Index: 2515.
    Returns: the number of times Jerry can throw things before being sent to the office.
    """
    # L1
    points_per_interruption = 5 # 5 points for interrupting
    interruptions = 2 # interrupted twice
    interruption_points = points_per_interruption * interruptions

    # L2
    points_per_insult = 10 # 10 points for insulting their classmates
    insults = 4 # insulted his classmates 4 times
    insult_points = points_per_insult * insults

    # L3
    point_limit = 100 # 100 points, they have to go to the office
    points_left = point_limit - interruption_points - insult_points

    # L4
    points_per_throw = 25 # 25 points for throwing things
    remaining_throws = points_left / points_per_throw

    # FA
    answer = remaining_throws
    return answer