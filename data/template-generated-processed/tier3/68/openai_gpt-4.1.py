from fractions import Fraction

def solve():
    """Index: 68.
    Returns: the number of coins Amalie will remain with after spending.
    """
    # L1
    elsa_ratio = 10 # ratio of coins Elsa has
    amalie_ratio = 45 # ratio of coins Amalie has
    total_ratio = elsa_ratio + amalie_ratio

    # L2
    total_coins = 440 # total number of coins they have
    amalie_fraction = Fraction(amalie_ratio, total_ratio)
    amalie_coins = amalie_fraction * total_coins

    # L3
    spent_fraction = Fraction(3, 4) # Amalie spends 3/4 of what she has
    coins_spent = spent_fraction * amalie_coins

    # L4
    coins_remaining = amalie_coins - coins_spent

    # FA
    answer = coins_remaining
    return answer