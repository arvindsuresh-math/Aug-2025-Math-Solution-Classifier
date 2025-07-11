from fractions import Fraction

def solve():
    """Index: 750.
    Returns: the total cost of the crayons.
    """
    # L1
    dozen_items = 12 # WK
    half_fraction = Fraction(1, 2) # WK
    half_dozen_items = half_fraction * dozen_items

    # L2
    num_half_dozens = 4 # 4 half dozen colored crayons
    total_crayons = num_half_dozens * half_dozen_items

    # L3
    cost_per_crayon = 2 # $2 per crayon
    total_cost = cost_per_crayon * total_crayons

    # FA
    answer = total_cost
    return answer