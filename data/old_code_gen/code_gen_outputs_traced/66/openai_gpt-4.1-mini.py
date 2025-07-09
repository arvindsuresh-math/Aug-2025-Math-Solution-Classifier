def solve(
    laptop_cost: int = 1000,  # laptop costs $1000
    down_payment_percent: float = 20,  # 20% down payment
    extra_down_payment: int = 20,  # Tara wants to pay an additional $20 for the down payment
    monthly_installment: int = 65,  # payment in installments of $65 per month
    months_paid: int = 4  # after paying for 4 months
):
    """Index: 66.
    Returns: the balance remaining after paying for 4 months.
    """

    #: L1
    down_payment = laptop_cost * down_payment_percent / 100 # eval: 200.0 = 1000 * 20 / 100

    #: L2
    total_down_payment = down_payment + extra_down_payment # eval: 220.0 = 200.0 + 20

    #: L3
    remaining_balance = laptop_cost - total_down_payment # eval: 780.0 = 1000 - 220.0

    #: L4
    monthly_payment = remaining_balance / 12 # eval: 65.0 = 780.0 / 12

    #: L5
    total_paid_4_months = monthly_payment * months_paid # eval: 260.0 = 65.0 * 4

    #: L6
    balance_after_4_months = remaining_balance - total_paid_4_months # eval: 520.0 = 780.0 - 260.0

    #: FA
    answer = balance_after_4_months
    return answer # eval: return 520.0
