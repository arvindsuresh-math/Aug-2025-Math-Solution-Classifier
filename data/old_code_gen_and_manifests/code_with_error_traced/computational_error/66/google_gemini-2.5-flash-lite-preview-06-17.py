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
    initial_down_payment = 190.0 # eval: 190.0 = 190.0

    #: L2
    total_down_payment = initial_down_payment + additional_down_payment # eval: 210.0 = 190.0 + 20

    #: L3
    remaining_balance = laptop_cost - total_down_payment # eval: 790.0 = 1000 - 210.0

    #: L4
    monthly_installment_payment = remaining_balance / 12 # eval: 65.83333333333333 = 790.0 / 12

    #: L5
    total_paid_in_installments = monthly_installment_payment * months_to_pay # eval: 263.3333333333333 = 65.83333333333333 * 4

    #: L6
    balance_after_payments = remaining_balance - total_paid_in_installments # eval: 526.6666666666667 = 790.0 - 263.3333333333333

    #: FA
    answer = balance_after_payments
    return answer # eval: return 526.6666666666667
