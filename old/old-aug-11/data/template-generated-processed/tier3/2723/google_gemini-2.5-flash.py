def solve():
    """Index: 2723.
    Returns: the length of the straight part of the river.
    """
    # L4
    total_river_length = 80 # If the river is 80 miles long
    # The problem states "The length of the straight part of a river is three times shorter than the crooked part."
    # This implies that the total river length is composed of 1 part straight and 3 parts crooked, making 4 total parts.
    total_parts_in_river = 4 # The length of the straight part of a river is three times shorter than the crooked part (1 part straight + 3 parts crooked)
    straight_part_length = total_river_length / total_parts_in_river

    # FA
    answer = straight_part_length
    return answer