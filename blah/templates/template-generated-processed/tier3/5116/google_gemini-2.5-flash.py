def solve():
    """Index: 5116.
    Returns: the amount of dollars Marge has left for fun.
    """
    # L1
    total_lottery_winnings = 12006 # $12006
    tax_divisor = 2 # half of the lottery amount
    money_after_taxes = total_lottery_winnings / tax_divisor

    # L2
    student_loan_divisor = 3 # a third of the leftover money
    paid_for_student_loans = money_after_taxes / student_loan_divisor

    # L3
    money_after_student_loans = money_after_taxes - paid_for_student_loans

    # L4
    savings_amount = 1000 # $1000 in savings
    money_after_savings = money_after_student_loans - savings_amount

    # L5
    investment_divisor = 5 # a fifth of that amount
    invested_amount = savings_amount / investment_divisor

    # L6
    money_left_for_fun = money_after_savings - invested_amount

    # FA
    answer = money_left_for_fun
    return answer