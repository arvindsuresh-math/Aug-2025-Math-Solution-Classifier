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
    total_ratio = 45 # eval: 45 = 45

    #: L2
    amalie_coins = (ratio_amalie / total_ratio) * total_coins # eval: 440.0 = (45 / 45) * 440

    #: L3
    coins_spent = fraction_spent * amalie_coins # eval: 330.0 = 0.75 * 440.0

    #: L4
    coins_remaining = amalie_coins - coins_spent # eval: 110.0 = 440.0 - 330.0

    #: FA
    answer = coins_remaining
    return answer # eval: return 110.0
