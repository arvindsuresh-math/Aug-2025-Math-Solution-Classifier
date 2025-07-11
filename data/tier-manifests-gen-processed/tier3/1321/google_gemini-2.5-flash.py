from fractions import Fraction

def solve():
    """Index: 1321.
    Returns: the total amount Pauline will spend including sales tax.
    """
    # L1
    sales_tax_percentage = Fraction(8, 100) # Sales tax is 8%
    total_before_tax = 150 # The total amount of all the items she wants to buy add up to $150
    sales_tax_amount = sales_tax_percentage * total_before_tax

    # L2
    total_after_tax = total_before_tax + sales_tax_amount

    # FA
    answer = total_after_tax
    return answer