def solve():
    """Index: 2016.
    Returns: the amount of money Vikki takes home after deductions.
    """
    # L1
    hourly_pay_rate = 10 # Her hourly pay rate is $10
    hours_worked = 42 # Vikki worked 42 hours in one week
    weekly_earnings = hourly_pay_rate * hours_worked

    # L2
    tax_rate = 0.2 # 20% is deducted as tax
    tax_deduction = weekly_earnings * tax_rate

    # L3
    insurance_rate = 0.05 # 5% is deducted as insurance cover
    insurance_deduction = weekly_earnings * insurance_rate

    # L4
    union_dues = 5 # $5 is deducted for union dues

    # L5
    total_deductions = tax_deduction + insurance_deduction + union_dues

    # L6
    answer = weekly_earnings - total_deductions
    return answer