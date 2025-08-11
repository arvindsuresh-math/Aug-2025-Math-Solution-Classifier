def solve():
    """Index: 322.
    Returns: the amount charged for gratuities.
    """
    # L1
    steak_cost = 80 # NY Striploin for $80
    wine_cost = 10 # a glass of wine for $10
    bill_before_tax_gratuity = steak_cost + wine_cost

    # L2
    sales_tax_percent = 10 # sales tax in my city is 10%
    percent_to_decimal_factor = 0.01 # WK
    taxes_paid = bill_before_tax_gratuity * sales_tax_percent * percent_to_decimal_factor

    # L3
    bill_before_gratuities = bill_before_tax_gratuity + taxes_paid

    # L4
    final_bill = 140 # total bill was $140
    gratuities_charged = final_bill - bill_before_gratuities

    # FA
    answer = gratuities_charged
    return answer