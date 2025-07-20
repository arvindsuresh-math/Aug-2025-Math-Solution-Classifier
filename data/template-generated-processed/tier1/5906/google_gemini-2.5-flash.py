def solve():
    """Index: 5906.
    Returns: the total length of the race.
    """
    # L1
    num_other_members = 4 # four other members on the team
    distance_per_member = 3 # run 3 km
    distance_other_members = num_other_members * distance_per_member

    # L2
    ralph_multiplier = 2 # twice as much
    ralph_distance = ralph_multiplier * distance_per_member

    # L3
    total_race_length = ralph_distance + distance_other_members

    # FA
    answer = total_race_length
    return answer