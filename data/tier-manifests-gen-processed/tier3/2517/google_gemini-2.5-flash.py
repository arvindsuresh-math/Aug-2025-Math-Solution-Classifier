from fractions import Fraction

def solve():
    """Index: 2517.
    Returns: the selling price of the house.
    """
    # L1
    original_price = 80000 # Mrs. Choi purchased a house for $80000
    profit_percentage = Fraction(20, 100) # sold it for a 20% profit
    profit_amount = original_price * profit_percentage

    # L2
    commission_percentage = Fraction(5, 100) # got a 5% broker's commission from the original price
    commission_amount = original_price * commission_percentage

    # L3
    selling_price = original_price + profit_amount + commission_amount

    # FA
    answer = selling_price
    return answer