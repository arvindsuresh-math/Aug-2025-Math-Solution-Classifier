def solve():
    """Index: 4988.
    Returns: the amount Tessa still owes Greg.
    """
    # L1
    initial_debt = 40 # lent her $40
    paid_back_divisor = 2 # paid him back half of her debt
    amount_paid_back = initial_debt / paid_back_divisor

    # L2
    debt_after_payment = initial_debt - amount_paid_back

    # L3
    additional_loan = 10 # asked him for $10 more
    final_debt = debt_after_payment + additional_loan

    # FA
    answer = final_debt
    return answer