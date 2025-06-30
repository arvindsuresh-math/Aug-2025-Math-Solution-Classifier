def solve(
        ratio_elsa: int = 10, # The ratio of coins that Elsa has is 10
        ratio_amalie: int = 45, # to that which Amalie has is 45
        total_coins: int = 440, # If the total number of coins they have is 440
        fraction_spent_amalie: float = 3/4 # Amalie spends 3/4 of what she has on toys
    ):
    """Index: 68.
    Returns: the number of coins Amalie has remaining after spending a fraction of them.
    """

    #: L1
    total_ratio = ratio_elsa + ratio_amalie # eval: 55 = 10 + 45

    #: L2
    amalie_coins = (ratio_amalie / total_ratio) * total_coins # eval: 360.0 = (45 / 55) * 440

    #: L3
    coins_spent_amalie = fraction_spent_amalie * amalie_coins # eval: 270.0 = 0.75 * 360.0

    #: L4
    remaining_coins_amalie = amalie_coins - coins_spent_amalie # eval: 90.0 = 360.0 - 270.0

    #: FA
    answer = remaining_coins_amalie # eval: 90.0 = 90.0
    return answer # eval: return 90.0
