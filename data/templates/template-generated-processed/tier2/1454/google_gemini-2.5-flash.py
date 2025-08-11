def solve():
    """Index: 1454.
    Returns: the total amount Tom has to pay in a year for the car lease.
    """
    # L1
    total_days_in_week = 7 # WK
    short_drive_days = 4 # 50 miles on Monday, Wednesday, and Friday, and Sunday (4 days)
    long_drive_days = total_days_in_week - short_drive_days

    # L2
    short_drive_miles = 50 # drives 50 miles
    long_drive_miles = 100 # drives 100 miles
    weekly_miles = short_drive_days * short_drive_miles + long_drive_days * long_drive_miles

    # L3
    cost_per_mile = 0.1 # $.1 per mile
    weekly_mileage_cost = weekly_miles * cost_per_mile

    # L4
    weekly_fee = 100 # weekly fee of $100
    total_weekly_cost = weekly_fee + weekly_mileage_cost

    # L5
    weeks_per_year = 52 # WK
    annual_cost = total_weekly_cost * weeks_per_year

    # FA
    answer = annual_cost
    return answer