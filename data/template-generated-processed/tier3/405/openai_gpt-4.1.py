def solve():
    """Index: 405.
    Returns: the maximum number of boats that can race in the river.
    """
    # L1
    boat_width = 3 # each boat is 3 feet across
    side_space = 2 # at least 2 feet between them or the riverbank
    feet_per_boat = boat_width + side_space

    # L2
    river_width = 42 # river that is 42 feet across
    last_boat_extra_space = 2 # additional 2 feet space on its other side
    usable_river_width = river_width - last_boat_extra_space

    # L3
    max_boats = usable_river_width / feet_per_boat

    # FA
    answer = max_boats
    return answer