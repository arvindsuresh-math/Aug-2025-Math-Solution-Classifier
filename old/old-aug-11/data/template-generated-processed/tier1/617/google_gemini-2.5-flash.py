def solve():
    """Index: 617.
    Returns: the total amount Mark owes for the speeding ticket.
    """
    # L1
    actual_speed = 75 # He was going 75 miles per hour
    speed_limit = 30 # in a 30 mile per hour zone
    speed_over_limit = actual_speed - speed_limit

    # L2
    fine_per_mph = 2 # increased by $2 for every mile per hour
    per_mile_fine_amount = fine_per_mph * speed_over_limit

    # L3
    base_fine = 50 # The base fine for speeding is $50
    fine_before_doubling = per_mile_fine_amount + base_fine

    # L4
    doubling_factor = 2 # The fine is also doubled
    fine_after_doubling = fine_before_doubling * doubling_factor

    # L5
    lawyer_hourly_rate = 80 # pay his lawyer $80/hour
    lawyer_hours = 3 # for three hours of work
    lawyer_fees = lawyer_hourly_rate * lawyer_hours

    # L6
    court_costs = 300 # pay $300 in court costs
    total_owed = lawyer_fees + court_costs + fine_after_doubling

    # FA
    answer = total_owed
    return answer