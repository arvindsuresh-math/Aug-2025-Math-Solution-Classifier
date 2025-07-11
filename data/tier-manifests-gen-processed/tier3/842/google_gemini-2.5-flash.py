from fractions import Fraction

def solve():
    """Index: 842.
    Returns: the number of meatballs Antonio will eat.
    """
    # L1
    hamburger_per_meatball = Fraction(1, 8) # 1/8 of a pound of hamburger per meatball
    total_hamburger = 4 # 4 pounds of hamburger
    reciprocal_of_hamburger_per_meatball = 8 # WK (reciprocal of 1/8)
    total_meatballs = total_hamburger / hamburger_per_meatball

    # L2
    num_family_members = 8 # 8 family members
    meatballs_per_person = total_meatballs / num_family_members

    # FA
    answer = meatballs_per_person
    return answer