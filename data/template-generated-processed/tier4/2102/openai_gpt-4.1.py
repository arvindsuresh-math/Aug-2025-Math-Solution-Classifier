def solve():
    """Index: 2102.
    Returns: the amount Maria has after deductions and utility bills payment.
    """
    # L1
    salary = 2000 # Maria's monthly salary is $2000
    tax_percent = 20 # 20% of her salary goes to paying tax
    percent_factor = 0.01 # WK
    tax_deduction = salary * tax_percent * percent_factor

    # L2
    insurance_percent = 5 # 5% goes to insurance
    insurance_deduction = salary * insurance_percent * percent_factor

    # L3
    total_deductions = tax_deduction + insurance_deduction

    # L4
    after_deductions = salary - total_deductions

    # L5
    utility_divisor = 4 # a quarter of the money left after the deductions is spent on utility bills
    utility_bills = after_deductions / utility_divisor

    # L6
    after_utilities = after_deductions - utility_bills

    # FA
    answer = after_utilities
    return answer