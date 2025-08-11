def solve():
    """Index: 4414.
    Returns: the total height John climbed.
    """
    # L1
    num_flights = 3 # 3 flights of stairs
    feet_per_flight = 10 # Each flight is 10 feet
    stairs_height = num_flights * feet_per_flight

    # L2
    rope_height_divisor = 2 # half that height
    rope_height = stairs_height / rope_height_divisor

    # L3
    ladder_extra_height = 10 # 10 feet longer than the rope
    ladder_height = rope_height + ladder_extra_height

    # L4
    total_height = stairs_height + rope_height + ladder_height

    # FA
    answer = total_height
    return answer