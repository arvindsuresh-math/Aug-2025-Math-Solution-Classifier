def solve():
    """Index: 5373.
    Returns: the amount of money on Jim's paycheck after deductions.
    """
    # L1
    gross_pay = 1120 # Jim’s bi-weekly gross pay is $1120
    retirement_percent_decimal = 0.25 # 25% of his paycheck go into his retirement account
    retirement_deduction = retirement_percent_decimal * gross_pay

    # L2
    pay_after_retirement = gross_pay - retirement_deduction

    # L3
    tax_deduction = 100.00 # take $100.00 out of each paycheck for taxes
    final_paycheck_amount = pay_after_retirement - tax_deduction

    # FA
    answer = final_paycheck_amount
    return answer