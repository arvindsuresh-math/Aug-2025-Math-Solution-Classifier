from fractions import Fraction

def solve():
    """Index: 68.
    Returns: the number of coins Amalie will remain with.
    """
    # L1
    elsa_ratio_part = 10 # The ratio of coins that Elsa has to that which Amalie has is 10:45
    amalie_ratio_part = 45 # The ratio of coins that Elsa has to that which Amalie has is 10:45
    total_ratio_parts = elsa_ratio_part + amalie_ratio_part

    # L2
    amalie_ratio_fraction = Fraction(amalie_ratio_part, total_ratio_parts) # The fraction of the ratio representing the number of coins that Amalie has is 45/55
    total_coins = 440 # the total number of coins they have is 440
    amalie_coins = amalie_ratio_fraction * total_coins

    # L3
    spent_fraction = Fraction(3, 4) # Amalie spends 3/4 of what she has
    coins_spent = spent_fraction * amalie_coins

    # L4
    remaining_coins = amalie_coins - coins_spent

    # FA
    answer = remaining_coins
    return answer