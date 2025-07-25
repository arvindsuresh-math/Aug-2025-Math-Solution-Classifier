def solve():
    """Index: 3912.
    Returns: the total price of the car.
    """
    # L1
    months_per_year = 12 # WK
    loan_years = 5 # 5 year loan
    loan_months = months_per_year * loan_years

    # L2
    monthly_payment = 250.00 # monthly payment $250.00
    total_loan_payment = monthly_payment * loan_months

    # L3
    down_payment = 5000.00 # $5,000.00 down as a down payment
    car_price = down_payment + total_loan_payment

    # FA
    answer = car_price
    return answer