def solve():
    """Index: 4443.
    Returns: the total number of horses on the carousel.
    """
    # L1
    blue_horses = 3 # 3 blue horses
    purple_multiplier = 3 # three times that many purple horses
    purple_horses = blue_horses * purple_multiplier

    # L2
    green_multiplier = 2 # twice as many green horses as purple horses
    green_horses = purple_horses * green_multiplier

    # L3
    gold_divisor = 6 # 1/6th as many gold horses as green horses
    gold_horses = green_horses / gold_divisor

    # L4
    total_horses = purple_horses + green_horses + gold_horses + blue_horses

    # FA
    answer = total_horses
    return answer