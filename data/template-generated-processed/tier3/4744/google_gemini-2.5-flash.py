def solve():
    """Index: 4744.
    Returns: the number of skill position players who must wait for the cooler to be refilled.
    """
    # L1
    num_linemen = 12 # 12 linemen
    ounces_per_lineman = 8 # drink 8 ounces each
    linemen_water_consumed = num_linemen * ounces_per_lineman

    # L2
    cooler_capacity = 126 # cooler holds 126 ounces of water
    remaining_water = cooler_capacity - linemen_water_consumed

    # L3
    ounces_per_skill_player = 6 # drink 6 ounces each
    skill_players_can_drink = remaining_water / ounces_per_skill_player

    # L4
    total_skill_players = 10 # 10 skill position players
    skill_players_waiting = total_skill_players - skill_players_can_drink

    # FA
    answer = skill_players_waiting
    return answer