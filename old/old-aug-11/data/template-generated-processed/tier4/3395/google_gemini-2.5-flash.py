from fractions import Fraction

def solve():
    """Index: 3395.
    Returns: how many times bigger Russia is than the United States.
    """
    # L1
    canada_us_ratio = 1.5 # Canada is 1.5 times bigger than the United States

    # L2
    russia_canada_increase_fraction = Fraction(1, 3) # Russia is 1/3 bigger than Canada
    russia_canada_multiplier_base = 1 # WK
    russia_canada_multiplier = russia_canada_multiplier_base + russia_canada_increase_fraction
    russia_us_ratio = canada_us_ratio * russia_canada_multiplier

    # FA
    answer = russia_us_ratio
    return answer