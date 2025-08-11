def solve():
    """Index: 2156.
    Returns: the distance Ryan can spit a watermelon seed in inches.
    """
    # L1
    billy_distance = 30 # Billy can spit a watermelon seed 30 inches
    madison_percent_num = 20 # 20% farther than Billy
    madison_percent_decimal = 0.20 # .20*30
    percent_factor = 0.01 # WK
    madison_extra_distance = madison_percent_num * percent_factor * billy_distance

    # L2
    madison_distance = billy_distance + madison_extra_distance

    # L3
    ryan_percent_num = 50 # 50% shorter than Madison
    ryan_percent_decimal = 0.50 # .50*36
    ryan_shorter_distance = ryan_percent_num * percent_factor * madison_distance
    ryan_distance = ryan_shorter_distance

    # FA
    answer = ryan_distance
    return answer