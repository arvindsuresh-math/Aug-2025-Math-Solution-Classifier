from fractions import Fraction

def solve():
    """Index: 627.
    Returns: the total cost to buy a table and 4 chairs.
    """
    # L1
    table_cost = 140 # a table costs $140
    chair_fraction = Fraction(1, 7) # 1/7 of the cost of a table
    cost_one_chair = table_cost * chair_fraction

    # L2
    num_chairs = 4 # 4 chairs
    cost_four_chairs = cost_one_chair * num_chairs

    # L3
    total_cost = table_cost + cost_four_chairs

    # FA
    answer = total_cost
    return answer