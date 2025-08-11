from fractions import Fraction

def solve():
    """Index: 6367.
    Returns: the amount of money Bert made on the sale.
    """
    # L1
    sale_price = 90 # bought a barrel for $90
    price_markup = 10 # sells them for $10 more
    warehouse_cost = sale_price - price_markup

    # L2
    tax_percentage = Fraction(10, 100) # pay 10% of the value in tax
    tax_amount = tax_percentage * sale_price

    # L3
    money_earned = sale_price - tax_amount - warehouse_cost

    # FA
    answer = money_earned
    return answer