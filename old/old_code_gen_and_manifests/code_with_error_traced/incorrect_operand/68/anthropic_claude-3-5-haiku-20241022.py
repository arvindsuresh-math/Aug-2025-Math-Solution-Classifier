def solve(
        elsa_ratio: int = 10,  # ratio of coins Elsa has
        amalie_ratio: int = 45,  # ratio of coins Amalie has
        total_coins: int = 440,  # total number of coins they have
        fraction_spent: float = 3/4  # Amalie spends 3/4 of her coins
    ):
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending."""

    #: L1
    total_ratio = elsa_ratio + amalie_ratio # eval: 55 = 10 + 45

    #: L2
    amalie_coins = (amalie_ratio / total_ratio) * total_coins # eval: 360.0 = (45 / 55) * 440

    #: L3
    coins_spent = fraction_spent * amalie_coins # eval: 270.0 = 0.75 * 360.0

    #: L4
    coins_remaining = amalie_coins - elsa_ratio # eval: 350.0 = 360.0 - 10

    #: FA
    answer = coins_remaining
    return answer # eval: return 350.0
