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

    #: L3
    coins_spent_amalie = fraction_spent_amalie * ratio_elsa # eval: 7.5 = 0.75 * 10

    #: L4
    remaining_coins_amalie = ratio_elsa - coins_spent_amalie # eval: 2.5 = 10 - 7.5

    #: FA
    answer = remaining_coins_amalie
    return answer # eval: return 2.5
