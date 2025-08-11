from fractions import Fraction

def solve():
    """Index: 2087.
    Returns: the amount of money each organization will receive.
    """
    # L1
    total_raised = 2500 # $2500 to be used for charity
    donation_percentage = Fraction(80, 100) # 80% to a public foundation
    donated_amount = total_raised * donation_percentage

    # L2
    num_organizations = 8 # 8 organizations
    amount_per_organization = donated_amount / num_organizations

    # FA
    answer = amount_per_organization
    return answer