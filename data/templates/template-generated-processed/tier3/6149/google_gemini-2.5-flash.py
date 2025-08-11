def solve():
    """Index: 6149.
    Returns: the total weight Jasmine has to carry in pounds.
    """
    # L1
    chip_bag_weight = 20 # A bag of chips weighs 20 ounces
    num_chip_bags = 6 # Jasmine buys 6 bags of chips
    total_chip_weight_ounces = chip_bag_weight * num_chip_bags

    # L2
    cookie_tins_multiplier = 4 # 4 times as many tins of cookies
    num_cookie_tins = num_chip_bags * cookie_tins_multiplier

    # L3
    cookie_tin_weight = 9 # a tin of cookies weighs 9 ounces
    total_cookie_weight_ounces = cookie_tin_weight * num_cookie_tins

    # L4
    total_weight_ounces = total_chip_weight_ounces + total_cookie_weight_ounces

    # L5
    ounces_per_pound = 16 # WK
    total_weight_pounds = total_weight_ounces / ounces_per_pound

    # FA
    answer = total_weight_pounds
    return answer