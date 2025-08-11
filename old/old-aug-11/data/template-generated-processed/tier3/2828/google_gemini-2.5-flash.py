def solve():
    """Index: 2828.
    Returns: the total number of magnets Peter has.
    """
    # L1
    total_magnets_adam_has = 18 # Adam has 18 magnets
    fraction_given_away_denominator = 3 # a third of the magnets
    magnets_given_away = total_magnets_adam_has / fraction_given_away_denominator

    # L2
    magnets_adam_left = total_magnets_adam_has - magnets_given_away

    # L3
    peter_multiplier = 2 # half as many magnets as Peter (meaning Peter has twice as many)
    peter_magnets = magnets_adam_left * peter_multiplier

    # FA
    answer = peter_magnets
    return answer