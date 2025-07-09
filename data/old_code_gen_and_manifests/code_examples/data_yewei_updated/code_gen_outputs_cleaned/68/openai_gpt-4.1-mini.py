def solve(
    ratio_elsa: int = 10,  # The ratio of coins that Elsa has
    ratio_amalie: int = 45,  # The ratio of coins that Amalie has
    total_coins: int = 440,  # The total number of coins they have
    fraction_spent: float = 3/4  # Amalie spends 3/4 of what she has
):
    """Index: 68.
    Returns: the number of coins Amalie remains with after spending 3/4 of her coins.
    """
    #: L1
    total_ratio = ratio_elsa + ratio_amalie

    #: L2
    amalie_coins = (ratio_amalie / total_ratio) * total_coins

    #: L3
    coins_spent = fraction_spent * amalie_coins

    #: L4
    coins_remaining = amalie_coins - coins_spent

    answer = coins_remaining  # FINAL ANSWER
    return answer