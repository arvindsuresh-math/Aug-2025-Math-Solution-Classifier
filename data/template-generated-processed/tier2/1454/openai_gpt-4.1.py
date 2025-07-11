def solve():
    """Index: 1454.
    Returns: the total amount Tom has to pay in a year for the car lease.
    """
    # L1
    days_in_week = 7 # WK
    short_drive_days = 4 # drives 50 miles on Monday, Wednesday, Friday, and Sunday
    long_drive_days = days_in_week - short_drive_days

    # L2
    short_drive_miles = 50 # drives 50 miles on short drive days
    long_drive_miles = 100 # drives 100 miles on other days
    total_miles_per_week = short_drive_days * short_drive_miles + long_drive_days * long_drive_miles

    # L3
    cost_per_mile = 0.1 # $.1 per mile
    mileage_cost_per_week = total_miles_per_week * cost_per_mile

    # L4
    weekly_fee = 100 # weekly fee of $100
    total_weekly_cost = weekly_fee + mileage_cost_per_week

    # L5
    weeks_per_year = 52 # WK
    total_yearly_cost = total_weekly_cost * weeks_per_year

    # FA
    answer = total_yearly_cost
    return answer