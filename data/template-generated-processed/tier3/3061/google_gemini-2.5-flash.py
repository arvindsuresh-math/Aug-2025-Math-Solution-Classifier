from fractions import Fraction

def solve():
    """Index: 3061.
    Returns: the amount of money Mikaela saved.
    """
    # L1
    first_month_hours = 35 # tutored for 35 hours
    additional_hours_second_month = 5 # 5 hours more than the first month
    second_month_hours = first_month_hours + additional_hours_second_month

    # L2
    total_tutoring_hours = first_month_hours + second_month_hours

    # L3
    hourly_rate = 10 # $10 an hour
    total_earnings = total_tutoring_hours * hourly_rate

    # L4
    expense_fraction = Fraction(4, 5) # 4/5 of her total earnings
    total_expenses = expense_fraction * total_earnings

    # L5
    amount_saved = total_earnings - total_expenses

    # FA
    answer = amount_saved
    return answer