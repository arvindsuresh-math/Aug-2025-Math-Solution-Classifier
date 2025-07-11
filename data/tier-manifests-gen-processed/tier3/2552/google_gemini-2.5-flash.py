def solve():
    """Index: 2552.
    Returns: the total number of dolls Dina has.
    """
    # L1
    collectors_edition_dolls = 20 # If Ivy has 20 collectors edition dolls
    fraction_numerator = 2 # 2/3 of Ivy's dolls
    fraction_denominator = 3 # 2/3 of Ivy's dolls
    ivy_total_dolls = collectors_edition_dolls / fraction_numerator * fraction_denominator

    # L2
    dina_multiplier = 2 # Dina has twice as many dolls as Ivy
    dina_total_dolls = ivy_total_dolls * dina_multiplier

    # FA
    answer = dina_total_dolls
    return answer