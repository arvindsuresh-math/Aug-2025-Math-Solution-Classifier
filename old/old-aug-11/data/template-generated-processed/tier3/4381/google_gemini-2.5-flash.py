def solve():
    """Index: 4381.
    Returns: the number of times Danny folded the blankets.
    """
    # L1
    blanket_side_length = 8 # area of 8 x 8
    area_each_blanket = blanket_side_length * blanket_side_length

    # L2
    num_blankets = 3 # three picnics blankets
    total_unfolded_area = num_blankets * area_each_blanket

    # L3
    folded_total_area = 48 # their total area is 48 square feet
    times_folded = total_unfolded_area / folded_total_area

    # FA
    answer = times_folded
    return answer