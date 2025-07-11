def solve():
    """Index: 1174.
    Returns: the number of blue butterflies Martha has.
    """
    # L1
    total_butterflies = 11 # Martha has 11 butterflies in her collection
    black_butterflies = 5 # If Martha has 5 black butterflies
    blue_and_yellow_butterflies = total_butterflies - black_butterflies

    # L2
    ratio_sum = 3 # WK
    yellow_butterflies = blue_and_yellow_butterflies / ratio_sum

    # L3
    blue_to_yellow_ratio = 2 # twice as many blue butterflies as yellow butterflies
    blue_butterflies = blue_to_yellow_ratio * yellow_butterflies

    # FA
    answer = blue_butterflies
    return answer