def solve(
    rent1: int = 800,  # the first apartment costs $800 per month in rent
    utilities1: int = 260,  # additional $260 per month in utilities
    rent2: int = 900,  # the second apartment costs $900 per month
    utilities2: int = 200,  # will cost an additional $200 per month in utilities
    miles_per_day1: int = 31,  # drive 31 miles per day to get to work
    miles_per_day2: int = 21,  # would only have to drive 21 miles to get to work
    cost_per_mile: float = 0.58,  # each mile has an average cost of 58 cents
    days_per_month: int = 20  # must drive to work 20 days each month
):
    """Index: 1202.
    Returns: the difference in total monthly costs of the two apartments after factoring in utilities and driving costs."""
    #: L1
    mileage_cost1 = miles_per_day1 * days_per_month * cost_per_mile
    #: L2
    total_cost1 = mileage_cost1 + rent1 + utilities1
    #: L3
    mileage_cost2 = miles_per_day2 * days_per_month * cost_per_mile
    #: L4
    total_cost2 = mileage_cost2 + rent2 + utilities2
    #: L5
    cost_difference = total_cost1 - total_cost2
    answer = cost_difference  # FINAL ANSWER
    return answer