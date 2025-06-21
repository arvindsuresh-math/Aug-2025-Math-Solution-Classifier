def solve(
    rent1: int = 800, # The first apartment costs $800 per month in rent
    utilities1: int = 260, # will cost an additional $260 per month in utilities
    rent2: int = 900, # The second apartment costs $900 per month
    utilities2: int = 200, # will cost an additional $200 per month in utilities
    miles1: int = 31, # drive 31 miles per day to get to work (first apartment)
    miles2: int = 21, # would only have to drive 21 miles to get to work (second apartment)
    cost_per_mile: float = 0.58, # each mile a person drives has an average cost of 58 cents
    days_per_month: int = 20 # the man must drive to work 20 days each month
):
    """Index: 1202.
    Returns: the difference in total monthly costs between the two apartments, rounded to the nearest dollar.
    """
    #: L1
    mileage_cost1 = miles1 * days_per_month * cost_per_mile

    #: L2
    total_cost1 = mileage_cost1 + rent1 + utilities1

    #: L3
    mileage_cost2 = miles2 * days_per_month * cost_per_mile

    #: L4
    total_cost2 = mileage_cost2 + rent2 + utilities2

    #: L5
    difference = round(total_cost1 - total_cost2)

    answer = difference # FINAL ANSWER
    return answer