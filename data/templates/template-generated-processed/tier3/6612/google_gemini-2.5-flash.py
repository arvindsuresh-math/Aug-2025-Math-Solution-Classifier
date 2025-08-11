def solve():
    """Index: 6612.
    Returns: the number of weeks it would take Camila to achieve her goal.
    """
    # L1
    camila_hikes = 7 # Camila has only gone hiking 7 times
    amanda_multiplier = 8 # Amanda has gone on 8 times as many hikes as Camila
    amanda_hikes = camila_hikes * amanda_multiplier

    # L2
    steven_additional_hikes = 15 # Steven has gone on 15 more hikes than Amanda
    steven_hikes = amanda_hikes + steven_additional_hikes

    # L3
    hikes_camila_needs = steven_hikes - camila_hikes

    # L4
    hikes_per_week = 4 # plans to go on 4 hikes a week
    weeks_to_achieve_goal = hikes_camila_needs / hikes_per_week

    # FA
    answer = weeks_to_achieve_goal
    return answer