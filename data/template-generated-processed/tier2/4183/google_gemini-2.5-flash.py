def solve():
    """Index: 4183.
    Returns: how much more John pays in taxes now compared to then.
    """
    # L1
    old_tax_rate_decimal = 0.2 # tax rate of 20%
    old_income = 1000000 # making 1,000,000 a year
    old_tax_paid = old_tax_rate_decimal * old_income

    # L2
    new_income = 1500000 # to 1,500,000 a year
    new_tax_rate_decimal = 0.3 # raised it to 30%
    new_tax_paid = new_income * new_tax_rate_decimal

    # L3
    tax_difference = new_tax_paid - old_tax_paid

    # FA
    answer = tax_difference
    return answer