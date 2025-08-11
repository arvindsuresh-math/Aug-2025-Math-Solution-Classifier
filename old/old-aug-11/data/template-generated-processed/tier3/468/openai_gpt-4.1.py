from fractions import Fraction

def solve():
    """Index: 468.
    Returns: the total amount Kevin has to pay for all items, including sales tax.
    """
    # L1
    tshirt_qty = 6 # six T-shirts
    tshirt_price = 8 # T-shirts at $8 each
    tshirt_total = tshirt_qty * tshirt_price

    # L2
    sweater_qty = 4 # four sweaters
    sweater_price = 18 # a sweater at $18
    sweater_total = sweater_qty * sweater_price

    # L3
    jacket_qty = 5 # five jackets
    jacket_price = 80 # a jacket at $80
    jacket_normal_total = jacket_qty * jacket_price

    # L4
    jacket_discount_rate = Fraction(10, 100) # 10% discount
    jacket_discount = jacket_discount_rate * jacket_normal_total

    # L5
    jacket_sale_total = jacket_normal_total - jacket_discount

    # L6
    total_items_cost = tshirt_total + sweater_total + jacket_sale_total

    # L7
    sales_tax_rate = Fraction(5, 100) # sales tax is 5%
    sales_tax = sales_tax_rate * total_items_cost

    # L8
    answer = total_items_cost + sales_tax
    return answer