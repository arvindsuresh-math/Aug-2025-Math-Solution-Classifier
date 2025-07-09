def solve(
    laptop_cost: int = 1000, # Tara has been planning to buy a laptop which costs $1000.
    down_payment_percentage: float = 0.20, # a 20% down payment is made.
    additional_down_payment: int = 20, # If Tara wants to pay an additional $20 for the down payment
    months_to_pay: int = 4 # after paying for 4 months?
):
    """Index: 66.
    Returns: Tara's balance after paying for 4 months.
    """

    #: L1
    initial_down_payment = laptop_cost * down_payment_percentage # eval: 200.0 = 1000 * 0.2

    #: L2
    total_down_payment = initial_down_payment + additional_down_payment # eval: 220.0 = 200.0 + 20

    #: L3

    #: L4
    monthly_installment_payment = months_to_pay / 12 # eval: 0.3333333333333333 = 4 / 12

    #: L5
    total_paid_in_installments = monthly_installment_payment * months_to_pay # eval: 1.3333333333333333 = 0.3333333333333333 * 4

    #: L6
    balance_after_payments = months_to_pay - total_paid_in_installments # eval: 2.666666666666667 = 4 - 1.3333333333333333

    #: FA
    answer = balance_after_payments
    return answer # eval: return 2.666666666666667
