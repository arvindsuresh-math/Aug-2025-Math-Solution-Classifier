from fractions import Fraction

def solve():
    """Index: 181.
    Returns: the total growth of the tree.
    """
    # L1
    initial_height = 100 # 100 meters tall
    growth_percentage = Fraction(10, 100) # 10% more than its previous height
    growth_2018 = initial_height * growth_percentage

    # L2
    height_end_2018 = initial_height + growth_2018

    # L3
    growth_2019 = height_end_2018 * growth_percentage

    # L4
    height_end_2019 = height_end_2018 + growth_2019

    # L5
    total_growth = height_end_2019 - initial_height

    # FA
    answer = total_growth
    return answer