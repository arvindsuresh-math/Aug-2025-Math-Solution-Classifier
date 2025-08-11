from fractions import Fraction

def solve():
    """Index: 4173.
    Returns: the number of burgers Jack can make.
    """
    # L1
    ketchup_cups = 3 # 3 cups of ketchup
    vinegar_cups = 1 # 1 cup of vinegar
    honey_cups = 1 # 1 cup of honey
    total_sauce_cups = ketchup_cups + vinegar_cups + honey_cups

    # L2
    sauce_per_pulled_pork_fraction = Fraction(1, 6) # 1/6 cup
    num_pulled_pork_sandwiches = 18 # 18 pulled pork sandwiches
    sauce_for_pulled_pork = sauce_per_pulled_pork_fraction * num_pulled_pork_sandwiches

    # L3
    sauce_for_burgers = total_sauce_cups - sauce_for_pulled_pork

    # L4
    sauce_per_burger_fraction = Fraction(1, 4) # 1/4 cup of sauce
    num_burgers = sauce_for_burgers / sauce_per_burger_fraction

    # FA
    answer = num_burgers
    return answer