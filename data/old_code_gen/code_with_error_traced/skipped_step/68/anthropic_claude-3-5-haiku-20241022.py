def solve(
        elsa_ratio: int = 10,  # ratio of coins Elsa has
        amalie_ratio: int = 45,  # ratio of coins Amalie has
        total_coins: int = 440,  # total number of coins they have
        fraction_spent: float = 3/4  # Amalie spends 3/4 of her coins
    ):
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending."""

    #: L1

    #: L2
    amalie_coins = (amalie_ratio / elsa_ratio) * total_coins # eval: 1980.0 = (45 / 10) * 440

    #: L3
    coins_spent = fraction_spent * amalie_coins # eval: 1485.0 = 0.75 * 1980.0

    #: L4
    coins_remaining = amalie_coins - coins_spent # eval: 495.0 = 1980.0 - 1485.0

    #: FA
    answer = coins_remaining
    return answer # eval: return 495.0
