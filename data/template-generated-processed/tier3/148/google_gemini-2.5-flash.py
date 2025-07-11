from fractions import Fraction

def solve():
    """Index: 148.
    Returns: the amount of money Winwin was able to take home.
    """
    # L1
    initial_winnings = 50 # Winwin won $50 in a lottery
    tax_percentage = Fraction(20, 100) # paid 20% for the tax
    tax_amount = initial_winnings * tax_percentage

    # L2
    winnings_after_tax = initial_winnings - tax_amount

    # L3
    processing_fee = 5 # paid $5 for the processing fee
    take_home_amount = winnings_after_tax - processing_fee

    # FA
    answer = take_home_amount
    return answer