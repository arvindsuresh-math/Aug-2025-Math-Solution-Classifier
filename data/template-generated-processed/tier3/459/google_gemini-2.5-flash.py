from fractions import Fraction

def solve():
    """Index: 459.
    Returns: the total cost for Mr. Lucian to buy 4 lawnmowers.
    """
    # L1
    old_cost = 1800 # cost was $1800 a year ago
    fraction_less = Fraction(2, 5) # 2/5 times less
    additional_cost = fraction_less * old_cost

    # L2
    current_cost_per_lawnmower = old_cost + additional_cost

    # L3
    number_of_lawnmowers = 4 # buy 4 such lawnmowers
    total_cost_for_multiple_lawnmowers = current_cost_per_lawnmower * number_of_lawnmowers

    # FA
    answer = total_cost_for_multiple_lawnmowers
    return answer