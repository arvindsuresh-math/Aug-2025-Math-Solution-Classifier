def solve():
    """Index: 2598.
    Returns: the number of collectors edition dolls Ivy has.
    """
    # L1
    dina_dolls = 60 # Dina has 60 dolls
    dina_ivy_ratio = 2 # twice as many dolls as Ivy
    ivy_dolls = dina_dolls / dina_ivy_ratio

    # L2
    collectors_fraction_denominator = 3 # 2/3 of Ivy's dolls
    collectors_fraction_numerator = 2 # 2/3 of Ivy's dolls
    collectors_edition_dolls = ivy_dolls / collectors_fraction_denominator * collectors_fraction_numerator

    # FA
    answer = collectors_edition_dolls
    return answer