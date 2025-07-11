def solve():
    """Index: 2001.
    Returns: the total money spent on gas for the trip.
    """
    # L1
    first_drive_hours = 2 # drives for 2 hours
    first_drive_speed = 60 # at 60mph
    first_drive_distance = first_drive_hours * first_drive_speed

    # L2
    second_drive_hours = 3 # continues driving for 3 hours
    second_drive_speed = 50 # at 50 mph
    second_drive_distance = second_drive_hours * second_drive_speed

    # L3
    total_miles_driven = first_drive_distance + second_drive_distance

    # L4
    miles_per_gallon = 30 # drive for 30 miles on one gallon of gas
    gallons_of_gas_used = total_miles_driven / miles_per_gallon

    # L5
    cost_per_gallon = 2 # one gallon of gas costs $2
    total_gas_cost = gallons_of_gas_used * cost_per_gallon

    # FA
    answer = total_gas_cost
    return answer