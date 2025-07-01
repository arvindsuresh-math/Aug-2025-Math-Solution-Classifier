def solve(
        laptop_cost: int = 1000, # laptop which costs $1000
        down_payment_percentage: float = 0.20, # 20% down payment
        monthly_installment_rate_stated: int = 65, # installments of $65 per month
        additional_down_payment: int = 20, # an additional $20 for the down payment
        months_paid: int = 4 # after paying for 4 months
    ):
    """Index: 66.
    Returns: Tara's remaining balance after paying for 4 months.
    """

    #: L1
    initial_down_payment = laptop_cost * down_payment_percentage # eval: 200.0 = 1000 * 0.2

    #: L2
    total_down_payment = initial_down_payment + additional_down_payment # eval: 220.0 = 200.0 + 20

    #: L3
    remaining_balance_initial = laptop_cost - total_down_payment # eval: 780.0 = 1000 - 220.0

    #: L4
    monthly_payment_calculated = remaining_balance_initial / 12 # eval: 65.0 = 780.0 / 12

    #: L5
    total_paid_4_months = monthly_payment_calculated * months_paid # eval: 260.0 = 65.0 * 4

    #: L6
    final_balance = remaining_balance_initial - total_down_payment # eval: 560.0 = 780.0 - 220.0

    #: FA
    answer = final_balance
    return answer # eval: return 560.0
