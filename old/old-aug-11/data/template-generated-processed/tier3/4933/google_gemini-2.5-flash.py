from fractions import Fraction

def solve():
    """Index: 4933.
    Returns: the combined number of quarters and dimes after putting some quarters aside.
    """
    # L1
    total_dimes = 350 # If she has 350 dimes
    dimes_per_quarter_ratio = 5 # five times as many dimes as quarters
    initial_quarters = total_dimes / dimes_per_quarter_ratio

    # L2
    quarters_to_put_aside_fraction = Fraction(2, 5) # 2/5 of the quarters
    quarters_reduced_by = quarters_to_put_aside_fraction * initial_quarters

    # L3
    remaining_quarters = initial_quarters - quarters_reduced_by

    # L4
    total_combined_money = remaining_quarters + total_dimes

    # FA
    answer = total_combined_money
    return answer