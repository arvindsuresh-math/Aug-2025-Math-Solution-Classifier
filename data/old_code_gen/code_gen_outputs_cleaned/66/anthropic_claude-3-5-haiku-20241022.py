def solve(
    laptop_price: int = 1000,  # Tara has been planning to buy a laptop which costs $1000
    down_payment_percentage: float = 0.2,  # A computer shop accepts payment with a 20% down payment
    additional_down_payment: int = 20,  # Tara wants to pay an additional $20 for the down payment
    monthly_installment: int = 65,  # payment installments of $65 per month
    months_paid: int = 4  # how much will her balance be after paying for 4 months
):
    """Index: 66.
    Returns: Tara's remaining balance after 4 months of payments.
    """
    #: L1
    standard_down_payment = laptop_price * down_payment_percentage

    #: L2
    total_down_payment = standard_down_payment + additional_down_payment

    #: L3
    remaining_balance = laptop_price - total_down_payment

    #: L4
    # Monthly installment is already given in the problem statement

    #: L5
    total_payments = monthly_installment * months_paid

    #: L6
    balance_after_payments = remaining_balance - total_payments

    answer = balance_after_payments  # FINAL ANSWER
    return answer