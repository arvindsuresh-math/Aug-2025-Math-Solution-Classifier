from fractions import Fraction

def solve():
    """Index: 894.
    Returns: the number of Pennsylvania state quarters Nick has.
    """
    # L1
    total_quarters = 35 # 35 quarters
    state_quarter_fraction = Fraction(2, 5) # 2/5 of the quarters are state quarters
    num_state_quarters = total_quarters * state_quarter_fraction

    # L2
    pennsylvania_fraction = 0.50 # 50 percent of the state quarters are Pennsylvania
    num_pennsylvania_quarters = num_state_quarters * pennsylvania_fraction

    # FA
    answer = num_pennsylvania_quarters
    return answer