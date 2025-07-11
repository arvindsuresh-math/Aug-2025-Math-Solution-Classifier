from fractions import Fraction

def solve():
    """Index: 3592.
    Returns: the time it takes for Tom to finish the program.
    """
    # L1
    bs_years = 3 # 3 years to finish the BS
    phd_years = 5 # 5 years to finish the Ph.D
    normal_duration = bs_years + phd_years

    # L2
    time_fraction = Fraction(3, 4) # 3/4ths the time
    actual_duration = normal_duration * time_fraction

    # FA
    answer = actual_duration
    return answer