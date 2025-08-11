from fractions import Fraction

def solve():
    """Index: 7303.
    Returns: the difference in kilograms of rice kept by Mr. Llesis and given to Mr. Everest.
    """
    # L1
    total_rice = 50 # 50 kilograms of rice
    kept_fraction = Fraction(7, 10) # kept 7/10 of it
    rice_kept_by_llesis = total_rice * kept_fraction

    # L2
    rice_given_to_everest = total_rice - rice_kept_by_llesis

    # L3
    difference_in_rice = rice_kept_by_llesis - rice_given_to_everest

    # FA
    answer = difference_in_rice
    return answer