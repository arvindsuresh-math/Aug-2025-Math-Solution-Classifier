def solve():
    """Index: 2102.
    Returns: the amount of money Maria has after deductions and utility bills payment.
    """
    # L1
    monthly_salary = 2000 # Maria's monthly salary is $2000
    tax_percent_num = 20 # 20% of her salary goes to paying tax
    percent_factor = 0.01 # WK
    tax_deduction = monthly_salary * tax_percent_num * percent_factor

    # L2
    insurance_percent_num = 5 # 5% goes to insurance
    insurance_deduction = monthly_salary * insurance_percent_num * percent_factor

    # L3
    total_deductions = tax_deduction + insurance_deduction

    # L4
    money_after_deductions = monthly_salary - total_deductions

    # L5
    utility_divisor = 4 # a quarter of the money left after the deductions is spent on utility bills
    utility_bill_payment = money_after_deductions / utility_divisor

    # L6
    money_after_all_payments = money_after_deductions - utility_bill_payment

    # FA
    answer = money_after_all_payments
    return answer