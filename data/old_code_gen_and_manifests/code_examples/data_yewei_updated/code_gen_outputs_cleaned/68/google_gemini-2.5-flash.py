def solve(
        elsa_ratio: int = 10, # The ratio of coins that Elsa has to that which Amalie has is 10
        amalie_ratio: int = 45, # The ratio of coins that Elsa has to that which Amalie has is 45
        total_coins: int = 440, # If the total number of coins they have is 440
        fraction_spent_amalie: float = 3/4 # Amalie spends 3/4 of what she has
    ):
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending.
    """
    #: L1
    total_ratio = elsa_ratio + amalie_ratio

    #: L2
    amalie_has_coins = (amalie_ratio / total_ratio) * total_coins

    #: L3
    coins_spent = fraction_spent_amalie * amalie_has_coins

    #: L4
    remaining_coins = amalie_has_coins - coins_spent

    answer = remaining_coins # FINAL ANSWER
    return answer