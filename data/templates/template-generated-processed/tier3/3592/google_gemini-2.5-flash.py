from fractions import Fraction

def solve():
    """Index: 3592.
    Returns: the time it takes for Tom to finish the program.
    """
    # L1
    bs_years = 3 # 3 years to finish the BS
    phd_years = 5 # 5 years to finish the Ph.D.
    normal_program_duration = bs_years + phd_years

    # L2
    time_reduction_fraction = Fraction(3, 4) # 3/4ths the time
    actual_finish_time = normal_program_duration * time_reduction_fraction

    # FA
    answer = actual_finish_time
    return answer