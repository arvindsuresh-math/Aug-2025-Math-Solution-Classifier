from fractions import Fraction

def solve():
    """Index: 894.
    Returns: the number of Pennsylvania state quarters Nick has.
    """
    # L1
    total_quarters = 35 # Nick has 35 quarters
    state_quarters_fraction = Fraction(2, 5) # 2/5 of the quarters are state quarters
    state_quarters = total_quarters * state_quarters_fraction

    # L2
    pennsylvania_fraction = 0.50 # 50 percent of the state quarters are Pennsylvania
    pennsylvania_quarters = state_quarters * pennsylvania_fraction

    # FA
    answer = pennsylvania_quarters
    return answer