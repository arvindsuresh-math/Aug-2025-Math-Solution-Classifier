def solve(
    laptop_cost: int = 1000, # Tara has been planning to buy a laptop which costs $1000.
    down_payment_percentage: float = 0.20, # a 20% down payment is made.
    additional_down_payment: int = 20, # If Tara wants to pay an additional $20 for the down payment
    monthly_installment_payment: int = 65, # installments of $65 per month
    months_paid: int = 4 # after paying for 4 months
):
    """Index: 66.
    Returns: Tara's remaining balance after paying for 4 months.
    """
    #: L1
    initial_down_payment = laptop_cost * down_payment_percentage

    #: L2
    total_down_payment = initial_down_payment + additional_down_payment

    #: L3
    remaining_balance_after_down_payment = laptop_cost - total_down_payment

    #: L4
    # The problem statement mentions a monthly installment of $65, which is calculated as $780/12 = $65.
    # We will use the given monthly_installment_payment directly.
    # calculated_monthly_payment = remaining_balance_after_down_payment / 12

    #: L5
    total_paid_over_months = monthly_installment_payment * months_paid

    #: L6
    balance_after_payments = remaining_balance_after_down_payment - total_paid_over_months

    answer = balance_after_payments # FINAL ANSWER
    return answer