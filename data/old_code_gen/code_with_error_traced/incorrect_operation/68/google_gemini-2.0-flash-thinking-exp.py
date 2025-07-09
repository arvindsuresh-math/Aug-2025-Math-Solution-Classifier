def solve(
    elsa_ratio: int = 10, # The ratio of coins that Elsa has to that which Amalie has is 10:45
    amalie_ratio: int = 45, # The ratio of coins that Elsa has to that which Amalie has is 10:45
    total_coins: int = 440, # If the total number of coins they have is 440
    fraction_spent_by_amalie: float = 3/4 # Amalie spends 3/4 of what she has on toys
):
    """Index: 68.
    Returns: the number of coins Amalie remains with after spending some.
    """

    #: L1
    total_ratio_parts = elsa_ratio - amalie_ratio # eval: -35 = 10 - 45

    #: L2
    amalie_coins = (amalie_ratio / total_ratio_parts) * total_coins # eval: -565.7142857142858 = (45 / -35) * 440

    #: L3
    coins_spent_by_amalie = fraction_spent_by_amalie * amalie_coins # eval: -424.28571428571433 = 0.75 * -565.7142857142858

    #: L4
    amalie_remaining_coins = amalie_coins - coins_spent_by_amalie # eval: -141.42857142857144 = -565.7142857142858 - -424.28571428571433

    #: FA
    answer = amalie_remaining_coins
    return answer # eval: return -141.42857142857144
