def solve():
    """Index: 1756.
    Returns: the number of hours Madeline needs to work this month.
    """
    # L1
    rent = 1200 # needs $1200 to pay rent
    groceries = 400 # $400 for groceries
    medical = 200 # $200 for medical expenses
    utilities = 60 # $60 for utilities
    emergency_savings = 200 # save $200 in case of an emergency
    total_needed = rent + groceries + medical + utilities + emergency_savings

    # L2
    hourly_wage = 15 # makes $15 per hour
    hours_needed_exact = total_needed / hourly_wage

    # L3
    hours_needed = int(hours_needed_exact) + (1 if hours_needed_exact != int(hours_needed_exact) else 0)

    # FA
    answer = hours_needed
    return answer