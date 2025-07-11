from fractions import Fraction

def solve():
    """Index: 849.
    Returns: the number of balloons in the hot air balloon that remain intact.
    """
    # L1
    initial_fraction_blown_up = Fraction(1, 5) # 1/5 of the total number of balloons
    total_balloons = 200 # A hot air balloon with 200 balloons
    initial_blown_up_balloons = initial_fraction_blown_up * total_balloons

    # L2
    remaining_after_half_hour = total_balloons - initial_blown_up_balloons

    # L3
    multiplier_next_hour = 2 # twice the number of balloons
    additional_blown_up_balloons = multiplier_next_hour * initial_blown_up_balloons

    # L4
    final_intact_balloons = remaining_after_half_hour - additional_blown_up_balloons

    # FA
    answer = final_intact_balloons
    return answer