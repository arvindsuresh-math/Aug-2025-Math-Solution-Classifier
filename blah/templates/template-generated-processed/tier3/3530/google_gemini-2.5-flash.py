from fractions import Fraction

def solve():
    """Index: 3530.
    Returns: the amount Walter allocates for school.
    """
    # L1
    hourly_wage = 5 # earns $5 per hour
    hours_per_day = 4 # work 4 hours a day
    daily_earning = hourly_wage * hours_per_day

    # L2
    days_per_week = 5 # works 5 days a week
    weekly_earning = daily_earning * days_per_week

    # L3
    school_allocation_fraction = Fraction(3, 4) # allocates 3/4 of his weekly earning
    school_allocation = weekly_earning * school_allocation_fraction

    # FA
    answer = school_allocation
    return answer