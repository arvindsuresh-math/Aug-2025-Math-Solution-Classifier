def solve():
    """Index: 617.
    Returns: the total amount Mark owes for the speeding ticket.
    """
    # L1
    mark_speed = 75 # 75 miles per hour
    speed_limit = 30 # 30 mile per hour zone
    mph_over = mark_speed - speed_limit

    # L2
    per_mile_fine = 2 # $2 for every mile per hour over
    per_mile_total = per_mile_fine * mph_over

    # L3
    base_fine = 50 # base fine for speeding is $50
    fine_plus_base = per_mile_total + base_fine

    # L4
    school_zone_multiplier = 2 # doubled because he was in a school zone
    school_zone_fine = fine_plus_base * school_zone_multiplier

    # L5
    lawyer_hourly = 80 # $80/hour for lawyer
    lawyer_hours = 3 # three hours of work
    lawyer_fees = lawyer_hourly * lawyer_hours

    # L6
    court_costs = 300 # $300 in court costs
    total_owed = lawyer_fees + court_costs + school_zone_fine

    # FA
    answer = total_owed
    return answer