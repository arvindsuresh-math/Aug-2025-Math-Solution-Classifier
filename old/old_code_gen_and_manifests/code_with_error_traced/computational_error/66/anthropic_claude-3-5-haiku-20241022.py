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
    standard_down_payment = 199.0 # eval: 199.0 = 199.0

    #: L2
    total_down_payment = standard_down_payment + additional_down_payment # eval: 219.0 = 199.0 + 20

    #: L3
    remaining_balance = laptop_price - total_down_payment # eval: 781.0 = 1000 - 219.0

    #: L5
    total_payments = monthly_installment * months_paid # eval: 260 = 65 * 4

    #: L6
    balance_after_payments = remaining_balance - total_payments # eval: 521.0 = 781.0 - 260

    #: FA
    answer = balance_after_payments
    return answer # eval: return 521.0
