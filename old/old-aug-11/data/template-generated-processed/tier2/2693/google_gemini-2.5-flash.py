def solve():
    """Index: 2693.
    Returns: the total amount John pays in taxes.
    """
    # L1
    earned_income = 100000 # earned $100,000 for the year
    deductions = 30000 # $30,000 in deductions
    taxable_income = earned_income - deductions

    # L2
    first_bracket_amount = 20000 # The first $20,000 of taxable income
    lower_tax_rate = 0.1 # taxed at 10%
    tax_lower_rate = first_bracket_amount * lower_tax_rate

    # L3
    remaining_taxable_income = taxable_income - first_bracket_amount

    # L4
    higher_tax_rate = 0.2 # taxed at 20%
    tax_higher_rate = remaining_taxable_income * higher_tax_rate

    # L5
    total_tax_bill = tax_higher_rate + tax_lower_rate

    # FA
    answer = total_tax_bill
    return answer