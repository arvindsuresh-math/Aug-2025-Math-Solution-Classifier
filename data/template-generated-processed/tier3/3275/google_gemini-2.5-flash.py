def solve():
    """Index: 3275.
    Returns: the amount of cake Pierre ate in grams.
    """
    # L1
    total_cake_grams = 400 # A cake of 400 grams
    nathalie_fraction_denominator = 8 # one-eighth of the cake
    nathalie_ate_grams = total_cake_grams / nathalie_fraction_denominator

    # L2
    pierre_multiplier = 2 # double what Nathalie ate
    pierre_ate_grams = pierre_multiplier * nathalie_ate_grams

    # FA
    answer = pierre_ate_grams
    return answer