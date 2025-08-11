def solve():
    """Index: 3656.
    Returns: the difference in the number of pencils sharpened by electric and hand-crank sharpeners.
    """
    # L1
    minutes_to_convert = 6 # six minutes
    seconds_per_minute = 60 # A minute is 60 seconds
    total_seconds = minutes_to_convert * seconds_per_minute

    # L2
    hand_crank_time_per_pencil = 45 # forty-five seconds
    pencils_hand_crank = total_seconds / hand_crank_time_per_pencil

    # L3
    electric_time_per_pencil = 20 # twenty seconds
    pencils_electric = total_seconds / electric_time_per_pencil

    # L4
    difference_in_pencils = pencils_electric - pencils_hand_crank

    # FA
    answer = difference_in_pencils
    return answer