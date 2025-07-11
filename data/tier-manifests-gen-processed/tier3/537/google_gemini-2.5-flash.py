from fractions import Fraction

def solve():
    """Index: 537.
    Returns: the total combined monthly earnings of the experienced sailors.
    """
    # L1
    more_fraction = Fraction(1, 5) # 1/5 times more
    inexperienced_hourly_pay = 10 # $10 per hour
    additional_pay_per_hour = more_fraction * inexperienced_hourly_pay

    # L2
    experienced_hourly_pay = inexperienced_hourly_pay + additional_pay_per_hour

    # L3
    workweek_hours = 60 # 60-hour workweek
    experienced_weekly_pay = workweek_hours * experienced_hourly_pay

    # L4
    weeks_per_month = 4 # WK
    experienced_monthly_pay_per_sailor = weeks_per_month * experienced_weekly_pay

    # L5
    total_sailors = 17 # 17 sailors
    inexperienced_sailors = 5 # five inexperienced sailors
    num_experienced_sailors = total_sailors - inexperienced_sailors

    # L6
    total_experienced_monthly_earnings = num_experienced_sailors * experienced_monthly_pay_per_sailor

    # FA
    answer = total_experienced_monthly_earnings
    return answer