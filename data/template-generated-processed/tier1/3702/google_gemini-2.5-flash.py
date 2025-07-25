def solve():
    """Index: 3702.
    Returns: how much Janet will save by buying the purple tiles instead of the turquoise ones.
    """
    # L1
    first_wall_length = 5 # 5 feet by 8 feet
    first_wall_width = 8 # 5 feet by 8 feet
    first_wall_area = first_wall_length * first_wall_width

    # L2
    second_wall_length = 7 # 7 feet by 8 feet
    second_wall_width = 8 # 7 feet by 8 feet
    second_wall_area = second_wall_length * second_wall_width

    # L3
    total_area = first_wall_area + second_wall_area

    # L4
    tiles_per_square_foot = 4 # each square foot of wall takes 4 tiles
    total_tiles_needed = total_area * tiles_per_square_foot

    # L5
    turquoise_cost_per_tile = 13 # $13/tile
    purple_cost_per_tile = 11 # $11/tile
    cost_difference_per_tile = turquoise_cost_per_tile - purple_cost_per_tile

    # L6
    total_cost_difference = cost_difference_per_tile * total_tiles_needed

    # FA
    answer = total_cost_difference
    return answer