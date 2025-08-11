def solve():
    """Index: 1278.
    Returns: the total length in centimeters of the two pieces of yarn.
    """
    # L1
    green_length = 156 # green piece of yarn is 156 cm long

    # L2
    multiplier_red = 3 # three times the length of the green yarn
    red_extra = 8 # 8 cm more
    red_length = multiplier_red * green_length + red_extra

    # L3
    total_length = green_length + red_length

    # FA
    answer = total_length
    return answer