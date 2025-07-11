from fractions import Fraction

def solve():
    """Index: 627.
    Returns: the total cost to buy a table and 4 chairs.
    """
    # L1
    table_cost = 140 # a table costs $140
    chair_fraction = Fraction(1, 7) # chair costs 1/7 of the cost of a table
    chair_cost = table_cost * chair_fraction

    # L2
    num_chairs = 4 # 4 chairs
    four_chairs_cost = chair_cost * num_chairs

    # L3
    total_cost = table_cost + four_chairs_cost

    # FA
    answer = total_cost
    return answer