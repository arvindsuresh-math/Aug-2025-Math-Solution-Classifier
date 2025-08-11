from fractions import Fraction

def solve():
    """Index: 537.
    Returns: the total combined monthly earnings of the experienced sailors.
    """
    # L1
    more_fraction = Fraction(1, 5) # 1/5 times more than the inexperienced sailors
    inexperienced_hourly = 10 # $10 per hour
    more_per_hour = more_fraction * inexperienced_hourly

    # L2
    experienced_hourly = inexperienced_hourly + more_per_hour

    # L3
    weekly_hours = 60 # 60-hour workweek
    weekly_earnings = weekly_hours * experienced_hourly

    # L4
    weeks_per_month = 4 # 4 weeks in a month (standard assumption)
    monthly_earnings = weeks_per_month * weekly_earnings

    # L5
    total_crew = 17 # crew consisted of 17 sailors
    inexperienced_sailors = 5 # five inexperienced sailors
    experienced_sailors = total_crew - inexperienced_sailors

    # L6
    total_combined_earnings = experienced_sailors * monthly_earnings

    # FA
    answer = total_combined_earnings
    return answer