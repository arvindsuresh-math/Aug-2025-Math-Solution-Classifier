def solve():
    """Index: 7233.
    Returns: the number of black butterflies Martha has.
    """
    # L1
    blue_butterflies = 6 # If Martha has 6 blue butterflies
    twice_as_many_divisor = 2 # twice as many blue butterflies as yellow butterflies
    yellow_butterflies = blue_butterflies / twice_as_many_divisor

    # L2
    blue_and_yellow_butterflies = blue_butterflies + yellow_butterflies

    # L3
    total_butterflies = 19 # Martha has 19 butterflies in her collection
    black_butterflies = total_butterflies - blue_and_yellow_butterflies

    # FA
    answer = black_butterflies
    return answer