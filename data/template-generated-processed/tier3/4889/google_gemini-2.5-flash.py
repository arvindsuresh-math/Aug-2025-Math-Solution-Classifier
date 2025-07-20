from fractions import Fraction

def solve():
    """Index: 4889.
    Returns: the total cost to feed the chickens.
    """
    # L1
    total_fraction = 1 # WK
    duck_fraction = Fraction(1, 3) # 1/3 are ducks
    chicken_fraction = total_fraction - duck_fraction

    # L2
    total_birds = 15 # Peter has 15 birds
    num_chickens = total_birds * chicken_fraction

    # L3
    cost_per_chicken = 2 # costs $2 per bird
    total_cost = num_chickens * cost_per_chicken

    # FA
    answer = total_cost
    return answer