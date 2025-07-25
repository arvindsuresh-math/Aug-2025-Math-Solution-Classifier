from fractions import Fraction

def solve():
    """Index: 6456.
    Returns: the amount Mr. McPherson needs to raise to complete the rent.
    """
    # L1
    mrs_mcpherson_percentage = Fraction(30, 100) # 30% of the money
    total_rent = 1200 # rent is $1200 per year
    mrs_mcpherson_contribution = mrs_mcpherson_percentage * total_rent

    # L2
    mr_mcpherson_contribution = total_rent - mrs_mcpherson_contribution

    # FA
    answer = mr_mcpherson_contribution
    return answer