from fractions import Fraction

def solve():
    """Index: 7387.
    Returns: the amount of money Amanda will receive.
    """
    # L1
    hours_worked_per_day = 10 # works for 10 hours a day
    hourly_pay = 50 # makes $50.00 an hour
    total_daily_income = hours_worked_per_day * hourly_pay

    # L2
    withholding_percentage = Fraction(20, 100) # withhold 20% of Amanda's pay
    amount_withheld = withholding_percentage * total_daily_income

    # L3
    money_received = total_daily_income - amount_withheld

    # FA
    answer = money_received
    return answer