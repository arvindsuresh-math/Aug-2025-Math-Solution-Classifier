def solve():
    """Index: 109.
    Returns: the number of nuggets Alyssa ate.
    """
    # L1
    total_nuggets = 100 # 100 chicken nuggets
    keely_ate_multiple = 2 # twice as many as Alyssa
    kendall_ate_multiple_as_written = 3 # as stated in solution L1, though inconsistent with problem statement
    total_equation_coefficient = 5 # from 100 = 5A
    # L1 sets up the equation. The output variable represents the coefficient of A in the final equation of this line.
    coefficient_of_A = total_equation_coefficient

    # L2
    divisor = coefficient_of_A # divide each side by 5
    alyssa_nuggets = total_nuggets / divisor

    # FA
    answer = alyssa_nuggets
    return answer