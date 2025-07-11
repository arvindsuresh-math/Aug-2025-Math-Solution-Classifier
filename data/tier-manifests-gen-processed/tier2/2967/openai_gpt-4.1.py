def solve():
    """Index: 2967.
    Returns: the amount Mark can bench press.
    """
    # L1
    dave_weight = 175 # Dave weighs 175 pounds
    dave_multiplier = 3 # three times his body weight
    dave_bench = dave_weight * dave_multiplier

    # L2
    craig_percent_num = 20 # 20% of the amount Dave can
    craig_percent_decimal = 0.20 # .20*525
    percent_factor = 0.01 # WK
    craig_bench = craig_percent_num * percent_factor * dave_bench

    # L3
    mark_less = 50 # 50 pounds less than Craig
    mark_bench = craig_bench - mark_less

    # FA
    answer = mark_bench
    return answer