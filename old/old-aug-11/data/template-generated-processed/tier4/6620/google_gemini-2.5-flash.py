from fractions import Fraction

def solve():
    """Index: 6620.
    Returns: the combined savings of the three employees after four weeks.
    """
    # L1
    hourly_wage = 10 # earning $10 per hour
    hours_per_day = 10 # work 10 hours a day
    daily_earnings = hourly_wage * hours_per_day

    # L2
    days_per_week = 5 # five days a week
    num_weeks = 4 # after four weeks
    total_work_days = days_per_week * num_weeks

    # L3
    monthly_earnings = total_work_days * daily_earnings

    # L4
    robby_save_fraction = Fraction(2, 5) # Robby saves 2/5 of his salary
    robby_savings = robby_save_fraction * monthly_earnings

    # L5
    jaylene_save_fraction = Fraction(3, 5) # Jaylene saves 3/5 of his salary
    jaylene_savings = jaylene_save_fraction * monthly_earnings

    # L6
    miranda_save_fraction = 0.5 # Miranda saves half of her salary
    miranda_savings = miranda_save_fraction * monthly_earnings

    # L7
    total_combined_savings = miranda_savings + jaylene_savings + robby_savings

    # FA
    answer = total_combined_savings
    return answer