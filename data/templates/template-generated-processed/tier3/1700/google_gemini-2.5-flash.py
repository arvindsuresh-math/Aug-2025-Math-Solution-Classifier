def solve():
    """Index: 1700.
    Returns: the total money Mike needs to pay for the car.
    """
    # L1
    loan_amount = 20000 # take $20000 from the bank
    loan_rate_numerator = 15 # rate of 15%
    loan_rate_denominator = 100 # rate of 15%
    additional_payment_to_bank = loan_amount * loan_rate_numerator / loan_rate_denominator

    # L2
    car_price = 35000 # red car for $35000
    total_cost = car_price + additional_payment_to_bank

    # FA
    answer = total_cost
    return answer