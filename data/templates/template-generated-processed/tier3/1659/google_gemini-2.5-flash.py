from fractions import Fraction

def solve():
    """Index: 1659.
    Returns: the total number of pines and redwoods.
    """
    # L1
    pines_count = 600 # 600 pines
    redwood_percentage_increase = Fraction(20, 100) # 20% more
    additional_redwoods = redwood_percentage_increase * pines_count

    # L2
    total_redwoods = additional_redwoods + pines_count

    # L3
    total_pines_and_redwoods = total_redwoods + pines_count

    # FA
    answer = total_pines_and_redwoods
    return answer