def solve():
    """Index: 4433.
    Returns: the total yards of fencing for the playground and garden.
    """
    # L1
    side_length_playground = 27 # side length of 27 yards
    sides_in_square = 4 # WK
    perimeter_playground = side_length_playground * sides_in_square

    # L2
    length_garden = 12 # 12 yard
    width_garden = 9 # 9 yard
    perimeter_garden = 2 * (length_garden + width_garden)

    # L3
    total_fencing = perimeter_playground + perimeter_garden

    # FA
    answer = total_fencing
    return answer