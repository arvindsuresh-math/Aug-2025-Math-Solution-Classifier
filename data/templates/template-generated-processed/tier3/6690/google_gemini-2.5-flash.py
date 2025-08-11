def solve():
    """Index: 6690.
    Returns: the remaining budget.
    """
    # L1
    test_tube_fraction_numerator = 2 # two-thirds of that amount
    test_tube_fraction_denominator = 3 # two-thirds of that amount
    flask_cost = 150 # bought $150 worth of flasks
    intermediate_product = test_tube_fraction_numerator * flask_cost
    test_tube_cost = intermediate_product / test_tube_fraction_denominator

    # L2
    safety_gear_divisor = 2 # half of the test tube cost
    safety_gear_cost = test_tube_cost / safety_gear_divisor

    # L3
    total_spent = flask_cost + test_tube_cost + safety_gear_cost

    # L4
    initial_budget = 325 # $325 budget
    remaining_budget = initial_budget - total_spent

    # FA
    answer = remaining_budget
    return answer