def solve():
    """Index: 6308.
    Returns: the number of months the car will be fully paid for.
    """
    # L1
    total_car_cost = 13380 # $13,380
    initial_payment = 5400 # $5,400
    remaining_balance = total_car_cost - initial_payment

    # L2
    monthly_payment = 420 # $420 a month
    number_of_months = remaining_balance / monthly_payment

    # FA
    answer = number_of_months
    return answer