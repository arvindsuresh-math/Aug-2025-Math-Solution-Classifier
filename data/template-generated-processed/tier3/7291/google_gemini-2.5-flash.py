def solve():
    """Index: 7291.
    Returns: the weight of the 75 m roll.
    """
    # L1
    long_roll_length = 75 # 75 m roll
    short_roll_length = 25 # 25 m wire
    length_ratio = long_roll_length / short_roll_length

    # L2
    short_roll_weight = 5 # weighs 5 kg
    long_roll_weight = short_roll_weight * length_ratio

    # FA
    answer = long_roll_weight
    return answer