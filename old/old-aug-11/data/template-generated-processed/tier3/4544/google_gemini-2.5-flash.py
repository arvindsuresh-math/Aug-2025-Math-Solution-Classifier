from fractions import Fraction

def solve():
    """Index: 4544.
    Returns: Kendra's total earnings in the two years.
    """
    # L1
    kendra_increase_percentage = Fraction(20, 100) # 20% more money
    laurel_sales_2014 = 30000 # Laurel earned $30000 in 2014
    kendra_additional_sales_2015 = kendra_increase_percentage * laurel_sales_2014

    # L2
    kendra_sales_2015 = laurel_sales_2014 + kendra_additional_sales_2015

    # L3
    kendra_less_2014 = 8000 # Kendra made $8000 less
    kendra_sales_2014 = laurel_sales_2014 - kendra_less_2014

    # L4
    kendra_total_earnings = kendra_sales_2014 + kendra_sales_2015

    # FA
    answer = kendra_total_earnings
    return answer