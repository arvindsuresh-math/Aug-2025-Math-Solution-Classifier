def solve():
    """Index: 5274.
    Returns: the total amount spent on gas.
    """
    # L1
    miles_per_day = 75 # He drives 75 miles per day
    number_of_days = 10 # in 10 days
    total_miles_driven = miles_per_day * number_of_days

    # L2
    miles_per_gallon = 50 # 50 miles to the gallon
    gallons_used = total_miles_driven / miles_per_gallon

    # L3
    cost_per_gallon = 3 # gas is $3 per gallon
    total_cost_on_gas = gallons_used * cost_per_gallon

    # FA
    answer = total_cost_on_gas
    return answer