def solve():
    """Index: 5132.
    Returns: the total money earned by Cid.
    """
    # L1
    oil_change_cost = 20 # charges $20 for an oil change
    num_oil_changes = 5 # changed the oil of 5 cars
    earned_from_oil_change = oil_change_cost * num_oil_changes

    # L2
    repair_cost = 30 # charges $30 for a repair
    num_repairs = 10 # repaired 10 cars
    earned_from_repair = repair_cost * num_repairs

    # L3
    # Note: The solution line's multiplication order (15 x 5) is used for variable mapping to ensure direct substitution,
    # even though the question implies (cost x quantity) i.e., (5 x 15).
    num_cars_washed_in_solution = 15 # washed 15 cars
    cost_per_car_wash_in_solution = 5 # charges $5 for a car wash
    earned_from_car_wash = num_cars_washed_in_solution * cost_per_car_wash_in_solution

    # L4
    total_earned = earned_from_oil_change + earned_from_repair + earned_from_car_wash

    # FA
    answer = total_earned
    return answer