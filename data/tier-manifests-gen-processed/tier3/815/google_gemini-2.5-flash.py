def solve():
    """Index: 815.
    Returns: the number of bracelets Bingley has remaining.
    """
    # L1
    kelly_bracelets = 16 # Kelly gives Bingley a fourth of her 16 bracelets
    fraction_denominator = 4 # a fourth of her 16 bracelets
    bracelets_from_kelly = kelly_bracelets / fraction_denominator

    # L2
    initial_bingley_bracelets = 5 # Bingley has 5 bracelets
    bingley_total_after_kelly = initial_bingley_bracelets + bracelets_from_kelly

    # L3
    sister_fraction_denominator = 3 # a third of his bracelets
    bracelets_to_sister = bingley_total_after_kelly / sister_fraction_denominator

    # L4
    remaining_bracelets = bingley_total_after_kelly - bracelets_to_sister

    # FA
    answer = remaining_bracelets
    return answer