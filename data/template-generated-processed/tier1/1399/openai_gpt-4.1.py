def solve():
    """Index: 1399.
    Returns: the height of the highest wave Austin caught in feet.
    """
    # L1
    surfboard_length = 7 # 7-foot surfboard
    shortest_wave_more_than_surfboard = 3 # three feet higher than his 7-foot surfboard
    shortest_wave_height = surfboard_length + shortest_wave_more_than_surfboard

    # L2
    shortest_wave_more_than_austin = 4 # four feet higher than his height
    austin_height = shortest_wave_height - shortest_wave_more_than_austin

    # L3
    highest_wave_multiplier = 4 # four times his height
    highest_wave_more_than_4x = 2 # two feet higher than four times his height
    highest_wave_height = austin_height * highest_wave_multiplier + highest_wave_more_than_4x

    # FA
    answer = highest_wave_height
    return answer