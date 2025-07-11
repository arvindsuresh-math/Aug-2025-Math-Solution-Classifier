from fractions import Fraction

def solve():
    """Index: 806.
    Returns: the total amount Donna paid for the porcelain vase.
    """
    # L1
    original_price = 200 # originally priced at $200
    discount_percentage = Fraction(25, 100) # 25% off
    discount_amount = original_price * discount_percentage

    # L2
    sale_price = original_price - discount_amount

    # L3
    sales_tax_percentage = Fraction(10, 100) # paid 10% sales tax
    sales_tax_amount = sale_price * sales_tax_percentage

    # L4
    total_paid = sale_price + sales_tax_amount

    # FA
    answer = total_paid
    return answer