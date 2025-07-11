from fractions import Fraction

def solve():
    """Index: 1523.
    Returns: the total cost Jason spends on replacement and repairs.
    """
    # L1
    stove_cost = 1200 # $1200
    wall_fraction = Fraction(1, 6) # 1/6th as much
    wall_repair_cost = stove_cost * wall_fraction

    # L2
    total_cost = wall_repair_cost + stove_cost

    # FA
    answer = total_cost
    return answer