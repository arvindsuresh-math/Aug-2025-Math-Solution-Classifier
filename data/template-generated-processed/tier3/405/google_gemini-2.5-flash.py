def solve():
    """Index: 405.
    Returns: the number of boats that can race.
    """
    # L1
    space_per_side = 2 # at least 2 feet between them or the riverbank
    boat_width = 3 # 3 feet across
    feet_per_boat = space_per_side + boat_width

    # L2
    river_width = 42 # river that is 42 feet across
    remaining_river_width = river_width - space_per_side

    # L3
    num_boats = remaining_river_width / feet_per_boat

    # FA
    answer = num_boats
    return answer