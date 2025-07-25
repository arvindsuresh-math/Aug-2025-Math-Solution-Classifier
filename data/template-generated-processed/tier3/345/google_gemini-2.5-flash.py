def solve():
    """Index: 345.
    Returns: the total money Adam earned after taxes.
    """
    # L1
    daily_pay = 40 # Adam earns $40 daily
    tax_divisor = 10 # 10% of his money is deducted as taxes
    daily_tax_deduction = daily_pay / tax_divisor

    # L2
    daily_pay_after_tax = daily_pay - daily_tax_deduction

    # L3
    work_days = 30 # after 30 days of work
    total_earned_after_tax = daily_pay_after_tax * work_days

    # FA
    answer = total_earned_after_tax
    return answer