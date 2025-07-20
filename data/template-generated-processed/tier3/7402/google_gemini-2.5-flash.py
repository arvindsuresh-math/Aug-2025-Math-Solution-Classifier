def solve():
    """Index: 7402.
    Returns: the combined number of soldiers in beacon towers.
    """
    # L1
    great_wall_length = 7300 # Great wall was 7300 kilometers long
    tower_interval = 5 # towers were located at 5 kilometer intervals
    num_beacon_towers = great_wall_length / tower_interval

    # L2
    soldiers_per_tower = 2 # every tower had two soldiers
    total_soldiers = num_beacon_towers * soldiers_per_tower

    # FA
    answer = total_soldiers
    return answer