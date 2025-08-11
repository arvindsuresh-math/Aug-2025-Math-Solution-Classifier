def solve():
    """Index: 7146.
    Returns: the percentage of ginger in the spice paste, rounded to the nearest integer.
    """
    # L1
    ginger_tbsp = 3 # 3 tablespoons of ginger
    teaspoons_per_tablespoon = 3 # WK
    ginger_tsp = ginger_tbsp * teaspoons_per_tablespoon

    # L2
    garlic_tbsp = 2 # 2 tablespoons of garlic
    garlic_tsp = garlic_tbsp * teaspoons_per_tablespoon

    # L3
    mustard_tsp = 1 # 1 teaspoon of mustard
    chile_powder_multiplier = 4 # four times as much chile powder as mustard
    chile_powder_tsp = mustard_tsp * chile_powder_multiplier

    # L4
    cardamom_tsp = 1 # 1 teaspoon of cardamom
    total_spice_tsp = ginger_tsp + garlic_tsp + chile_powder_tsp + cardamom_tsp + mustard_tsp

    # L5
    percent_multiplier = 100 # WK
    ginger_percentage_unrounded = (ginger_tsp / total_spice_tsp) * percent_multiplier
    ginger_percentage = round(ginger_percentage_unrounded)

    # FA
    answer = ginger_percentage
    return answer