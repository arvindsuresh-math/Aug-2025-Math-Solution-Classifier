def solve():
    """Index: 3611.
    Returns: the total amount Dabbie spent on all the turkeys.
    """
    # L1
    weight_first_turkey = 6 # the first turkey is 6 kilograms
    cost_per_kg = 2 # the cost of a kilogram of turkey is $2
    cost_first_turkey = weight_first_turkey * cost_per_kg

    # L2
    weight_second_turkey = 9 # the second turkey is 9 kilograms
    cost_second_turkey = weight_second_turkey * cost_per_kg

    # L3
    multiplier_third_turkey = 2 # twice the weight of the second turkey
    weight_third_turkey = weight_second_turkey * multiplier_third_turkey

    # L4
    cost_third_turkey = weight_third_turkey * cost_per_kg

    # L5
    total_cost = cost_first_turkey + cost_second_turkey + cost_third_turkey

    # FA
    answer = total_cost
    return answer