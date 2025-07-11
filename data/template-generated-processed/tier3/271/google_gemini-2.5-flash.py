from fractions import Fraction

def solve():
    """Index: 271.
    Returns: the total amount of money Nadia used to buy the flowers.
    """
    # L1
    num_roses = 20 # 20 roses
    cost_per_rose = 5 # roses cost $5 each
    total_cost_roses = num_roses * cost_per_rose

    # L2
    lily_fraction = Fraction(3, 4) # 3/4 times as many Lillies
    num_lilies = lily_fraction * num_roses

    # L3
    lily_cost_multiplier = 2 # lilies cost twice as much each
    cost_per_lily = cost_per_rose * lily_cost_multiplier

    # L4
    total_cost_lilies = cost_per_lily * num_lilies

    # L5
    total_money_used = total_cost_lilies + total_cost_roses

    # FA
    answer = total_money_used
    return answer