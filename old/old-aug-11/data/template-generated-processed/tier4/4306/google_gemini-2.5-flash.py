def solve():
    """Index: 4306.
    Returns: the number of albino 8-antlered deer.
    """
    # L1
    total_deer = 920 # 920 deer in a park
    antler_percent_num = 10 # 10% of the deer have 8 antlers
    percent_factor = 0.01 # WK
    deer_with_8_antlers = total_deer * antler_percent_num * percent_factor

    # L2
    albino_fraction_divisor = 4 # a quarter of that number also have albino fur
    albino_8_antlered_deer = deer_with_8_antlers / albino_fraction_divisor

    # FA
    answer = albino_8_antlered_deer
    return answer