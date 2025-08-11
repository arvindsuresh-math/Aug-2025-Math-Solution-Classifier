def solve():
    """Index: 5862.
    Returns: the total cost of gas each month.
    """
    # L1
    total_monthly_mileage = 450 # 450-mile monthly driving mileage
    num_cars = 3 # three cars
    mileage_per_car = total_monthly_mileage / num_cars

    # L2
    mpg_car1 = 50 # first car averages 50 miles per gallon
    gallons_car1 = mileage_per_car / mpg_car1

    # L3
    mpg_car2 = 10 # second car averages 10 miles per gallon
    gallons_car2 = mileage_per_car / mpg_car2

    # L4
    mpg_car3 = 15 # third car averages 15 miles per gallon
    gallons_car3 = mileage_per_car / mpg_car3

    # L5
    total_gallons = gallons_car1 + gallons_car2 + gallons_car3

    # L6
    cost_per_gallon = 2 # gas costs $2 per gallon
    total_cost = total_gallons * cost_per_gallon

    # FA
    answer = total_cost
    return answer