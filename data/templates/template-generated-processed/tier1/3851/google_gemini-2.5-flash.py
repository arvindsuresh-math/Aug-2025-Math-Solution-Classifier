def solve():
    """Index: 3851.
    Returns: the total distance Peter has to fly.
    """
    # L1
    distance_spain_russia = 7019 # distance an airplane travels between Spain and Russia is 7019 km
    distance_spain_germany = 1615 # distance between Spain and Germany is 1615 km
    distance_germany_russia = distance_spain_russia - distance_spain_germany

    # L2
    total_distance_to_fly = distance_germany_russia + distance_spain_russia

    # FA
    answer = total_distance_to_fly
    return answer