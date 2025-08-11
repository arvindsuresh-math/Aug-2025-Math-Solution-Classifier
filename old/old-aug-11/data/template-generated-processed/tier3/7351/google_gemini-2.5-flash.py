def solve():
    """Index: 7351.
    Returns: the daily minimum amount Rita must pay.
    """
    # L1
    machine_cost = 120 # a $120 elliptical machine
    down_payment_divisor = 2 # half the cost of the machine
    down_payment = machine_cost / down_payment_divisor

    # L2
    balance = machine_cost - down_payment

    # L3
    payment_days = 10 # within 10 days
    daily_minimum_payment = balance / payment_days

    # FA
    answer = daily_minimum_payment
    return answer