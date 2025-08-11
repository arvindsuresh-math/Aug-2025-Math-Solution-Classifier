from fractions import Fraction

def solve():
    """Index: 468.
    Returns: the total amount Kevin has to pay for all items, including sales tax.
    """
    # L1
    num_tshirts = 6 # six T-shirts
    tshirt_price = 8 # T-shirts at $8 each
    cost_tshirts = num_tshirts * tshirt_price

    # L2
    num_sweaters = 4 # four sweaters
    sweater_price = 18 # a sweater at $18
    cost_sweaters = num_sweaters * sweater_price

    # L3
    num_jackets = 5 # five jackets
    jacket_normal_price = 80 # a jacket at $80
    normal_cost_jackets = num_jackets * jacket_normal_price

    # L4
    discount_percentage = Fraction(10, 100) # 10% discount
    discount_amount = discount_percentage * normal_cost_jackets

    # L5
    selling_price_jackets = normal_cost_jackets - discount_amount

    # L6
    total_cost_before_tax = cost_tshirts + cost_sweaters + selling_price_jackets

    # L7
    sales_tax_percentage = Fraction(5, 100) # sales tax is 5%
    sales_tax_amount = sales_tax_percentage * total_cost_before_tax

    # L8
    total_amount_to_pay = total_cost_before_tax + sales_tax_amount

    # FA
    answer = total_amount_to_pay
    return answer