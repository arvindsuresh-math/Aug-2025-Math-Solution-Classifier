def solve(
    ratio_elsa: int = 10, # The ratio of coins that Elsa has to that which Amalie has is 10:45
    ratio_amalie: int = 45, # The ratio of coins that Elsa has to that which Amalie has is 10:45
    total_coins: int = 440, # the total number of coins they have is 440
    amalie_fraction_spent: float = 3/4 # Amalie spends 3/4 of what she has on toys
):
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending some of them.
    """

    #: L1
    total_ratio = ratio_elsa + ratio_amalie # eval: 55 = 10 + 45

    #: L2
    amalie_coins = (ratio_amalie / total_ratio) * total_coins # eval: 360.0 = (45 / 55) * 440

    #: L3

    #: L4
    amalie_remaining_coins = amalie_coins - ratio_elsa # eval: 350.0 = 360.0 - 10

    #: FA
    answer = amalie_remaining_coins
    return answer # eval: return 350.0
