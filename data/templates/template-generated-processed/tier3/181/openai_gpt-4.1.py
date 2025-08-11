from fractions import Fraction

def solve():
    """Index: 181.
    Returns: the total growth of the tree from 2017 until the end of 2019 in meters.
    """
    # L1
    initial_height_2017 = 100 # 100 meters tall at the end of 2017
    growth_percent_numerator = 10 # 10% more than its previous height each year
    growth_percent_denominator = 100 # 10% more than its previous height each year
    growth_2018 = initial_height_2017 * Fraction(growth_percent_numerator, growth_percent_denominator)

    # L2
    height_2018 = initial_height_2017 + growth_2018

    # L3
    growth_2019 = height_2018 * Fraction(growth_percent_numerator, growth_percent_denominator)

    # L4
    height_2019 = height_2018 + growth_2019

    # L5
    total_growth = height_2019 - initial_height_2017

    # FA
    answer = total_growth
    return answer