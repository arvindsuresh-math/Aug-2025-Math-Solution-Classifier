from fractions import Fraction

def solve():
    """Index: 5865.
    Returns: the number of rotten apples that did not smell.
    """
    # L1
    rotten_percentage = Fraction(40, 100) # 40 percent were rotten
    total_apples = 200 # 200 apples
    rotten_apples = rotten_percentage * total_apples

    # L2
    smelling_percentage = Fraction(70, 100) # 70 percent of the rotten apples smelled
    smelling_rotten_apples = smelling_percentage * rotten_apples

    # L3
    non_smelling_rotten_apples = rotten_apples - smelling_rotten_apples

    # FA
    answer = non_smelling_rotten_apples
    return answer