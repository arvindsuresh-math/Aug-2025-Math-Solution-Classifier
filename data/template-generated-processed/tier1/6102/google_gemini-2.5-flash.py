def solve():
    """Index: 6102.
    Returns: the difference in cost between buying a new car and renting a car for a year.
    """
    # L1
    rent_cost_per_month = 20 # costs $20 per month
    months_per_year = 12 # WK
    rent_cost_per_year = rent_cost_per_month * months_per_year

    # L2
    new_car_cost_per_month = 30 # costs $30 per month
    new_car_cost_per_year = new_car_cost_per_month * months_per_year

    # L3
    cost_difference = new_car_cost_per_year - rent_cost_per_year

    # FA
    answer = cost_difference
    return answer