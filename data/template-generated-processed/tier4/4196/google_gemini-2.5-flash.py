from fractions import Fraction

def solve():
    """Index: 4196.
    Returns: the number of eggs that actually hatch.
    """
    # L1
    total_eggs_per_year = 30 # 30 eggs per year
    infertile_percent = 0.20 # 20 percent of them are infertile
    infertile_eggs = total_eggs_per_year * infertile_percent

    # L2
    eggs_after_infertile = total_eggs_per_year - infertile_eggs

    # L3
    calcification_fraction = Fraction(1, 3) # a third of the remaining eggs will not hatch
    calcification_eggs = eggs_after_infertile * calcification_fraction

    # L4
    hatchable_eggs = eggs_after_infertile - calcification_eggs

    # FA
    answer = hatchable_eggs
    return answer