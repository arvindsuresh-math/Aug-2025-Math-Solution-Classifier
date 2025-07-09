def solve(
    laptop_cost: int = 1000, # laptop which costs $1000
    monthly_installment: int = 65, # installments of $65 per month
    down_payment_percentage: float = 0.20, # a 20% down payment
    additional_down_payment: int = 20, # an additional $20 for the down payment
    months_paid: int = 4 # after paying for 4 months
):
    """Index: 66.
    Returns: the remaining balance after paying for a specified number of months.
    """

    #: L1
    required_down_payment = laptop_cost * down_payment_percentage # eval: 200.0 = 1000 * 0.2

    #: L2
    total_down_payment = required_down_payment + additional_down_payment # eval: 220.0 = 200.0 + 20

    #: L3
    remaining_balance_after_down_payment = laptop_cost - total_down_payment # eval: 780.0 = 1000 - 220.0

    #: L5
    total_paid_in_installments = monthly_installment * months_paid # eval: 260 = 65 * 4

    #: L6
    balance_after_installments = remaining_balance_after_down_payment - total_paid_in_installments # eval: 520.0 = 780.0 - 260

    #: FA
    answer = balance_after_installments
    return answer # eval: return 520.0
