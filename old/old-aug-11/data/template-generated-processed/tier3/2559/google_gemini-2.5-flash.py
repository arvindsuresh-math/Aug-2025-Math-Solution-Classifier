def solve():
    """Index: 2559.
    Returns: the cost of the old car in dollars.
    """
    # L1
    paid_from_old_car_sale = 1800 # He sold his old car for $1800 and used that to pay off some of the cost of his new car
    amount_still_owed = 2000 # He still owes another $2000 on his new car
    new_car_cost = paid_from_old_car_sale + amount_still_owed

    # L2
    new_car_cost_multiplier = 2 # Ben's new car cost twice as much as his old car
    old_car_cost = new_car_cost / new_car_cost_multiplier

    # FA
    answer = old_car_cost
    return answer