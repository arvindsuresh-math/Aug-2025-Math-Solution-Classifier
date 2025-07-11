def solve():
    """Index: 2693.
    Returns: the total amount John pays in taxes.
    """
    # L1
    total_income = 100000 # earned $100,000 for the year
    deductions = 30000 # $30,000 in deductions
    taxable_income = total_income - deductions

    # L2
    lower_bracket_limit = 20000 # first $20,000 of taxable income
    lower_rate = 0.1 # taxed at 10%
    lower_bracket_tax = lower_bracket_limit * lower_rate

    # L3
    higher_bracket_income = taxable_income - lower_bracket_limit

    # L4
    higher_rate = 0.2 # taxed at 20%
    higher_bracket_tax = higher_bracket_income * higher_rate

    # L5
    total_tax = higher_bracket_tax + lower_bracket_tax

    # FA
    answer = total_tax
    return answer