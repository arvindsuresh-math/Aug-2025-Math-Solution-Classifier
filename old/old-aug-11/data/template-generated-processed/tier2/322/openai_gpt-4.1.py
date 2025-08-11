def solve():
    """Index: 322.
    Returns: the amount charged for gratuities.
    """
    # L1
    steak_price = 80 # $80 for the steak
    wine_price = 10 # $10 for the wine
    pre_tax_total = steak_price + wine_price

    # L2
    tax_percent_num = 10 # sales tax in my city is 10%
    percent_factor = 0.01 # WK
    tax_amount = pre_tax_total * tax_percent_num * percent_factor

    # L3
    pre_gratuity_total = pre_tax_total + tax_amount

    # L4
    final_bill = 140 # my total bill was $140
    gratuity_amount = final_bill - pre_gratuity_total

    # FA
    answer = gratuity_amount
    return answer