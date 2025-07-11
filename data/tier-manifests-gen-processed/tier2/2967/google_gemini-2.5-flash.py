def solve():
    """Index: 2967.
    Returns: how much Mark can bench press.
    """
    # L1
    dave_weight = 175 # Dave weighs 175 pounds
    dave_multiplier = 3 # three times his body weight
    dave_bench_press = dave_weight * dave_multiplier

    # L2
    craig_percent_decimal = 0.20 # 20% of the amount Dave can
    craig_percent_num = 20 # 20% of the amount Dave can
    percent_factor = 0.01 # WK
    craig_bench_press = craig_percent_decimal * dave_bench_press

    # L3
    mark_less_amount = 50 # 50 pounds less than Craig
    mark_bench_press = craig_bench_press - mark_less_amount

    # FA
    answer = mark_bench_press
    return answer