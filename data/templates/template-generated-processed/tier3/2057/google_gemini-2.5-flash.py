def solve():
    """Index: 2057.
    Returns: the number of rocks Jack needs to hold.
    """
    # L1
    jack_weight = 60 # Jack, who weighs 60 pounds
    anna_weight = 40 # Anna, who weighs 40 pounds
    weight_difference = jack_weight - anna_weight

    # L2
    rock_weight = 4 # 4-pound rocks
    num_rocks = weight_difference / rock_weight

    # FA
    answer = num_rocks
    return answer