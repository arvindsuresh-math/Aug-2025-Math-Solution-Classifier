def solve(
    rent_apt1: int = 800, # The first apartment costs $800 per month in rent
    utilities_apt1: int = 260, # and will cost an additional $260 per month in utilities
    rent_apt2: int = 900, # The second apartment costs $900 per month
    utilities_apt2: int = 200, # and will cost an additional $200 per month in utilities
    distance_apt1: int = 31, # the man would have to drive 31 miles per day
    distance_apt2: int = 21, # the man would only have to drive 21 miles
    cost_per_mile: float = 0.58, # each mile a person drives has an average cost of 58 cents
    work_days_per_month: int = 20 # drive to work 20 days each month
):
    """Index: 1202.
    Returns: the difference in total monthly costs between the two apartments.
    """
    #: L1
    mileage_cost_apt1 = distance_apt1 * work_days_per_month * cost_per_mile

    #: L2
    total_cost_apt1 = mileage_cost_apt1 + rent_apt1 + utilities_apt1

    #: L3
    mileage_cost_apt2 = distance_apt2 * work_days_per_month * cost_per_mile

    #: L4
    total_cost_apt2 = mileage_cost_apt2 + rent_apt2 + utilities_apt2

    #: L5
    difference = total_cost_apt1 - total_cost_apt2

    answer = difference # FINAL ANSWER
    return answer