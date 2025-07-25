def solve():
    """Index: 4757.
    Returns: how much more flour, in ounces, Carrie brought than Katy.
    """
    # L1
    katy_num_bags = 3 # Katy brought three 5-pound bags of flour
    katy_bag_weight = 5 # 5-pound bags of flour
    katy_total_flour_pounds = katy_num_bags * katy_bag_weight

    # L2
    wendi_multiplier = 2 # twice as much flour as Katy
    wendi_total_flour_pounds = katy_total_flour_pounds * wendi_multiplier

    # L3
    carrie_less_than_wendi = 5 # 5 pounds less than the amount of flour Wendi brought
    carrie_total_flour_pounds = wendi_total_flour_pounds - carrie_less_than_wendi

    # L4
    difference_pounds = carrie_total_flour_pounds - katy_total_flour_pounds

    # L5
    ounces_per_pound = 16 # WK
    difference_ounces = difference_pounds * ounces_per_pound

    # FA
    answer = difference_ounces
    return answer