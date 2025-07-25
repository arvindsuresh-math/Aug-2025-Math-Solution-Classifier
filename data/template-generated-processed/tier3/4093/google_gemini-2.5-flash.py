from fractions import Fraction

def solve():
    """Index: 4093.
    Returns: the number of cases on which the judge ruled guilty.
    """
    # L1
    total_cases = 17 # seventeen court cases
    dismissed_cases = 2 # Two were immediately dismissed from court
    remaining_cases_after_dismissal = total_cases - dismissed_cases

    # L2
    innocent_fraction_numerator = 2 # Two-thirds of the remaining cases
    innocent_fraction_denominator = 3 # Two-thirds of the remaining cases
    innocent_fraction = Fraction(innocent_fraction_numerator, innocent_fraction_denominator)
    innocent_cases = innocent_fraction * remaining_cases_after_dismissal

    # L3
    delayed_cases = 1 # one ruling was delayed
    guilty_cases = remaining_cases_after_dismissal - innocent_cases - delayed_cases

    # FA
    answer = guilty_cases
    return answer