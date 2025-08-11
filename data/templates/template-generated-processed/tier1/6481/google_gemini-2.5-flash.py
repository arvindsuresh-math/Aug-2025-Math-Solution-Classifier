def solve():
    """Index: 6481.
    Returns: the difference in volume between the two birdhouses.
    """
    # L1
    sara_width_ft = 1 # 1 foot wide
    sara_height_ft = 2 # 2 feet tall
    sara_depth_ft = 2 # 2 feet deep
    inches_per_foot = 12 # WK
    sara_width_in = sara_width_ft * inches_per_foot
    sara_height_in = sara_height_ft * inches_per_foot
    sara_depth_in = sara_depth_ft * inches_per_foot

    # L2
    sara_volume = sara_width_in * sara_height_in * sara_depth_in

    # L3
    jake_width_in = 16 # 16 inches wide
    jake_height_in = 20 # 20 inches tall
    jake_depth_in = 18 # 18 inches deep
    jake_volume = jake_width_in * jake_height_in * jake_depth_in

    # L4
    volume_difference = sara_volume - jake_volume

    # FA
    answer = volume_difference
    return answer