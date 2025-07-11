def solve():
    """Index: 1202.
    Returns: the difference between the total monthly costs of the two apartments after factoring in utility and driving-related costs (to the nearest whole dollar).
    """
    # L1
    miles_per_day_apt1 = 31 # drive 31 miles per day to get to work (apartment 1)
    work_days_per_month = 20 # drive to work 20 days each month
    cost_per_mile = 0.58 # each mile a person drives has an average cost of 58 cents
    mileage_cost_apt1 = miles_per_day_apt1 * work_days_per_month * cost_per_mile

    # L2
    rent_apt1 = 800 # first apartment costs $800 per month in rent
    utilities_apt1 = 260 # will cost an additional $260 per month in utilities
    total_cost_apt1 = mileage_cost_apt1 + rent_apt1 + utilities_apt1

    # L3
    miles_per_day_apt2 = 21 # man would only have to drive 21 miles to get to work (apartment 2)
    mileage_cost_apt2 = miles_per_day_apt2 * work_days_per_month * cost_per_mile

    # L4
    rent_apt2 = 900 # second apartment costs $900 per month
    utilities_apt2 = 200 # will cost an additional $200 per month in utilities
    total_cost_apt2 = mileage_cost_apt2 + rent_apt2 + utilities_apt2

    # L5
    difference = total_cost_apt1 - total_cost_apt2
    answer = round(difference) # FA
    return answer