def solve(
        elsa_ratio: int = 10,  # ratio of coins Elsa has
        amalie_ratio: int = 45,  # ratio of coins Amalie has
        total_coins: int = 440,  # total number of coins they have
        fraction_spent: float = 3/4  # Amalie spends 3/4 of her coins
):
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending."""
    #: L1
    total_ratio = elsa_ratio + amalie_ratio

    #: L2
    amalie_coins = (amalie_ratio / total_ratio) * total_coins

    #: L3
    coins_spent = fraction_spent * amalie_coins

    #: L4
    coins_remaining = amalie_coins - coins_spent

    answer = coins_remaining  # FINAL ANSWER
    return answer