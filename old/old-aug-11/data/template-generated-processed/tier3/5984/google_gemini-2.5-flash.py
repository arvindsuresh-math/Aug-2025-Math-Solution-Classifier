from fractions import Fraction

def solve():
    """Index: 5984.
    Returns: the total sum of money shared.
    """
    # L1
    debby_percentage = 25 # Debby takes 25%
    total_percentage = 100 # WK
    maggie_percentage = total_percentage - debby_percentage

    # L2
    maggie_share_amount = 4500 # Maggie's share is $4,500
    maggie_fraction_of_total = Fraction(maggie_percentage, total_percentage)

    # L3
    inverse_maggie_fraction = Fraction(total_percentage, maggie_percentage)
    total_amount = inverse_maggie_fraction * maggie_share_amount

    # FA
    answer = total_amount
    return answer