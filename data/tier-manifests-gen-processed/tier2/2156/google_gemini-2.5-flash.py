def solve():
    """Index: 2156.
    Returns: how far Ryan can spit a watermelon seed.
    """
    # L1
    billy_distance = 30 # Billy can spit a watermelon seed 30 inches
    madison_farther_percent_num = 20 # 20% farther
    madison_farther_percent_decimal = 0.20 # from solution text: .20*30
    percent_factor = 0.01 # WK
    madison_extra_distance = madison_farther_percent_num * percent_factor * billy_distance

    # L2
    madison_total_distance = billy_distance + madison_extra_distance

    # L3
    ryan_shorter_percent_num = 50 # 50% shorter
    ryan_shorter_percent_decimal = 0.50 # from solution text: .50*36
    ryan_distance = ryan_shorter_percent_num * percent_factor * madison_total_distance

    # FA
    answer = ryan_distance
    return answer