def solve():
    """Index: 1202.
    Returns: the difference between the total monthly costs of the two apartments.
    """
    # L1
    miles_per_day_apt1 = 31 # drive 31 miles per day
    driving_days_per_month = 20 # drive to work 20 days each month
    cost_per_mile_dollars = 0.58 # 58 cents
    mileage_cost_apt1 = miles_per_day_apt1 * driving_days_per_month * cost_per_mile_dollars

    # L2
    rent_apt1 = 800 # $800 per month in rent
    utilities_apt1 = 260 # $260 per month in utilities
    total_cost_apt1 = mileage_cost_apt1 + rent_apt1 + utilities_apt1

    # L3
    miles_per_day_apt2 = 21 # drive 21 miles
    mileage_cost_apt2 = miles_per_day_apt2 * driving_days_per_month * cost_per_mile_dollars

    # L4
    rent_apt2 = 900 # $900 per month
    utilities_apt2 = 200 # $200 per month in utilities
    total_cost_apt2 = mileage_cost_apt2 + rent_apt2 + utilities_apt2

    # L5
    cost_difference = total_cost_apt1 - total_cost_apt2

    # FA
    answer = round(cost_difference)
    return answer