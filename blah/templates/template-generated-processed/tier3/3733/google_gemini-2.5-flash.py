from fractions import Fraction

def solve():
    """Index: 3733.
    Returns: the total bushels of corn Jorge's land yielded.
    """
    # L1
    total_acres = 60 # 60 acres of property
    clay_fraction = Fraction(1, 3) # One-third of Jorge's 60 acres
    clay_acres = total_acres * clay_fraction

    # L2
    good_soil_acres = total_acres - clay_acres

    # L3
    good_soil_yield_per_acre = 400 # yields 400 bushels per acre
    good_soil_total_bushels = good_soil_acres * good_soil_yield_per_acre

    # L4
    clay_soil_yield_divisor = 2 # only half as much per acre as in good soil
    clay_soil_yield_per_acre = good_soil_yield_per_acre / clay_soil_yield_divisor

    # L5
    clay_soil_total_bushels = clay_acres * clay_soil_yield_per_acre

    # L6
    total_bushels = good_soil_total_bushels + clay_soil_total_bushels

    # FA
    answer = total_bushels
    return answer