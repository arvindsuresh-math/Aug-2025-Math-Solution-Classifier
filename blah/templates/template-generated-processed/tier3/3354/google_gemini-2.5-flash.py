def solve():
    """Index: 3354.
    Returns: the amount Mr. Lalande has to pay every month.
    """
    # L1
    car_worth = 18000 # superb car worth 18000 €
    initial_payment = 3000 # pays 3,000 euros to be able to leave with the car
    remaining_to_pay = car_worth - initial_payment

    # L2
    num_installments = 6 # pay the rest in 6 monthly installments
    monthly_payment = remaining_to_pay / num_installments

    # FA
    answer = monthly_payment
    return answer