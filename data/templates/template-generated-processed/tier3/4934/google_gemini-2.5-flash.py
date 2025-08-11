from fractions import Fraction

def solve():
    """Index: 4934.
    Returns: the difference between Emma's and Briana's return-on-investment after 2 years.
    """
    # L1
    emma_roi_percentage = Fraction(15, 100) # Emma's investment is supposed to yield 15% of the capital annually
    emma_capital = 300 # Emma invested $300
    emma_annual_roi = emma_roi_percentage * emma_capital

    # L2
    num_years = 2 # after 2 years
    emma_total_roi = emma_annual_roi * num_years

    # L3
    briana_roi_percentage = Fraction(10, 100) # Briana's should yield 10% annually
    briana_capital = 500 # Briana invested $500
    briana_annual_roi = briana_roi_percentage * briana_capital

    # L4
    briana_total_roi = briana_annual_roi * num_years

    # L5
    roi_difference = briana_total_roi - emma_total_roi

    # FA
    answer = roi_difference
    return answer