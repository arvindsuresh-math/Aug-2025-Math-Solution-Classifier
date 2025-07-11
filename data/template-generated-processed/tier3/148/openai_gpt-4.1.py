from fractions import Fraction

def solve():
    """Index: 148.
    Returns: the amount Winwin was able to take home after tax and processing fee.
    """
    # L1
    winnings = 50 # Winwin won $50 in a lottery
    tax_percentage = Fraction(20, 100) # 20% for the tax
    tax_paid = winnings * tax_percentage

    # L2
    after_tax = winnings - tax_paid

    # L3
    processing_fee = 5 # $5 for the processing fee
    take_home = after_tax - processing_fee

    # FA
    answer = take_home
    return answer