def solve():
    """Index: 2174.
    Returns: the total cost of the aquarium.
    """
    # L1
    original_price = 120 # original price of $120
    discount_percentage_numerator = 50 # marked down 50%
    percentage_denominator = 100 # WK
    discount_amount = original_price * discount_percentage_numerator / percentage_denominator

    # L2
    marked_down_price = original_price - discount_amount

    # L3
    sales_tax_percentage_numerator = 5 # sales tax equal to 5%
    sales_tax_amount = marked_down_price * sales_tax_percentage_numerator / percentage_denominator

    # L4
    total_cost = marked_down_price + sales_tax_amount

    # FA
    answer = total_cost
    return answer