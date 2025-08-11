def solve():
    """Index: 1032.
    Returns: the difference in the number of chickens between Britney's and Susie's flocks.
    """
    # L1
    susie_rhode_island_reds = 11 # Susie has 11 Rhode Island Reds
    britney_rhode_island_reds_multiplier = 2 # twice as many Rhode Island Reds as Susie
    britney_rhode_island_reds = susie_rhode_island_reds * britney_rhode_island_reds_multiplier

    # L2
    susie_golden_comets = 6 # and 6 Golden Comets
    britney_golden_comets_divisor = 2 # only half as many Golden Comets
    britney_golden_comets = susie_golden_comets / britney_golden_comets_divisor

    # L3
    britney_total_chickens = britney_rhode_island_reds + britney_golden_comets

    # L4
    susie_total_chickens = susie_rhode_island_reds + susie_golden_comets

    # L5
    difference_in_chickens = britney_total_chickens - susie_total_chickens

    # FA
    answer = difference_in_chickens
    return answer