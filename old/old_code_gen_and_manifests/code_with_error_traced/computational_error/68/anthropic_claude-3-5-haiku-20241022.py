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
    amalie_coins = 361.0 # eval: 361.0 = 361.0

    #: L3
    coins_spent = fraction_spent * amalie_coins # eval: 270.75 = 0.75 * 361.0

    #: L4
    coins_remaining = amalie_coins - coins_spent # eval: 90.25 = 361.0 - 270.75

    #: FA
    answer = coins_remaining
    return answer # eval: return 90.25
