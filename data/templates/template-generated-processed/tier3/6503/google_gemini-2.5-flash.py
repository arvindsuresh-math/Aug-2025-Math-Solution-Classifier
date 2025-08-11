def solve():
    """Index: 6503.
    Returns: the difference in the number of monkeys and giraffes Carla saw.
    """
    # L1
    zebras = 12 # counted 12 zebras
    camel_ratio_divisor = 2 # only half as many camels as there were zebras
    camels = zebras / camel_ratio_divisor

    # L2
    monkeys_per_camel = 4 # 4 times the number of monkeys as camels
    monkeys = monkeys_per_camel * camels

    # L3
    giraffes = 2 # counted only 2 giraffes
    more_monkeys_than_giraffes = monkeys - giraffes

    # FA
    answer = more_monkeys_than_giraffes
    return answer