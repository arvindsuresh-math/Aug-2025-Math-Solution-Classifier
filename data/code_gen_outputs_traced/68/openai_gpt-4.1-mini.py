def solve(
    ratio_elsa: int = 10,  # ratio of coins Elsa has
    ratio_amalie: int = 45,  # ratio of coins Amalie has
    total_coins: int = 440,  # total number of coins they have
    fraction_spent: float = 3/4  # fraction of coins Amalie spends
):
    """Index: 68.
    Returns: the number of coins Amalie remains with after spending 3/4 of her coins.
    """

    #: L1
    total_ratio = ratio_elsa + ratio_amalie # eval: 55 = 10 + 45

    #: L2
    amalie_coins = (ratio_amalie / total_ratio) * total_coins # eval: 360.0 = (45 / 55) * 440

    #: L3
    coins_spent = fraction_spent * amalie_coins # eval: 270.0 = 0.75 * 360.0

    #: L4
    coins_remaining = amalie_coins - coins_spent # eval: 90.0 = 360.0 - 270.0

    #: FA
    answer = coins_remaining # eval: 90.0 = 90.0
    return answer # eval: return 90.0
