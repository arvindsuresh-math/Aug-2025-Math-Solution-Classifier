from fractions import Fraction

def solve():
    """Index: 6200.
    Returns: the number of units remaining from the contracted number.
    """
    # L1
    fraction_built_first_half = Fraction(3, 5) # 3/5 units of the contracted number
    contracted_houses = 2000 # 2000 houses
    units_built_first_half = fraction_built_first_half * contracted_houses

    # L2
    units_remaining_after_first_half = contracted_houses - units_built_first_half

    # L3
    additional_units_by_october = 300 # an additional 300 units
    final_units_remaining = units_remaining_after_first_half - additional_units_by_october

    # FA
    answer = final_units_remaining
    return answer