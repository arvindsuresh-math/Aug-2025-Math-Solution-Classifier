from fractions import Fraction

def solve():
    """Index: 3942.
    Returns: the total amount of money the firefighter has after paying monthly expenses.
    """
    # L1
    hourly_rate = 30 # $30 per hour
    work_hours_per_week = 48 # 48-hour workweek
    weekly_earnings = hourly_rate * work_hours_per_week

    # L2
    weeks_per_month = 4 # WK
    monthly_earnings = weekly_earnings * weeks_per_month

    # L3
    rent_fraction = Fraction(1, 3) # 1/3 of the money on rent
    monthly_rent = rent_fraction * monthly_earnings

    # L4
    food_cost = 500 # $500 on food
    taxes_cost = 1000 # $1000 on taxes
    total_monthly_expenses = monthly_rent + food_cost + taxes_cost

    # L5
    money_after_expenses = monthly_earnings - total_monthly_expenses

    # FA
    answer = money_after_expenses
    return answer