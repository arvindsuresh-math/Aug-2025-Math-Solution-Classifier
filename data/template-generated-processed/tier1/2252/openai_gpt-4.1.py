def solve():
    """Index: 2252.
    Returns: the distance between Mary and Jimmy after 1 hour.
    """
    # L1
    mary_speed = 5 # Mary runs at 5 miles per hour
    time = 1 # after 1 hour
    mary_distance = mary_speed * time

    # L2
    jimmy_speed = 4 # Jimmy runs at 4 miles per hour
    jimmy_distance = jimmy_speed * time

    # L3
    total_distance = mary_distance + jimmy_distance

    # FA
    answer = total_distance
    return answer