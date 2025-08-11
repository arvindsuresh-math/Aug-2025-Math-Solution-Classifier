from fractions import Fraction

def solve():
    """Index: 271.
    Returns: the total amount of money Nadia used to buy the flowers.
    """
    # L1
    num_roses = 20 # buy 20 roses
    cost_per_rose = 5 # roses cost $5 each
    total_cost_roses = num_roses * cost_per_rose

    # L2
    lilies_fraction = Fraction(3, 4) # 3/4 times as many Lillies as roses
    num_lilies = lilies_fraction * num_roses

    # L3
    cost_per_lily = cost_per_rose * 2 # lilies cost twice as much each

    # L4
    total_cost_lilies = cost_per_lily * num_lilies

    # L5
    total_cost = total_cost_lilies + total_cost_roses

    # FA
    answer = total_cost
    return answer