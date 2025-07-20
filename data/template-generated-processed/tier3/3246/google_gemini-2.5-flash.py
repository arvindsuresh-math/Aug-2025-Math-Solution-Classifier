def solve():
    """Index: 3246.
    Returns: the number of iron balls molded.
    """
    # L1
    bar_length = 12 # 12 cm
    bar_width = 8 # 8 cm
    bar_height = 6 # 6 cm
    volume_one_bar = bar_length * bar_width * bar_height

    # L2
    num_iron_bars = 10 # ten iron bars
    total_volume_bars = num_iron_bars * volume_one_bar

    # L3
    volume_each_ball = 8 # Each iron ball has a volume of 8 cubic cm
    num_iron_balls_molded = total_volume_bars / volume_each_ball

    # FA
    answer = num_iron_balls_molded
    return answer