def solve():
    """Index: 3118.
    Returns: Jason's total monthly payment for the car.
    """
    # L1
    car_cost = 32000 # The car he wants costs $32,000
    down_payment = 8000 # down payment of $8,000
    loan_amount = car_cost - down_payment

    # L2
    num_monthly_payments = 48 # make 48 equal monthly payments
    monthly_payment_before_interest = loan_amount / num_monthly_payments

    # L3
    interest_rate_decimal = 0.05 # interest equal to 5%
    monthly_interest = monthly_payment_before_interest * interest_rate_decimal

    # L4
    total_monthly_payment = monthly_payment_before_interest + monthly_interest

    # FA
    answer = total_monthly_payment
    return answer