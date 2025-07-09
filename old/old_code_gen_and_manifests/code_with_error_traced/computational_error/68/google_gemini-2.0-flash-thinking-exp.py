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
    total_ratio_parts = elsa_ratio + amalie_ratio # eval: 55 = 10 + 45

    #: L2
    amalie_coins = (amalie_ratio / total_ratio_parts) * total_coins # eval: 360.0 = (45 / 55) * 440

    #: L3
    coins_spent_by_amalie = 269.0 # eval: 269.0 = 269.0

    #: L4
    amalie_remaining_coins = amalie_coins - coins_spent_by_amalie # eval: 91.0 = 360.0 - 269.0

    #: FA
    answer = amalie_remaining_coins
    return answer # eval: return 91.0
