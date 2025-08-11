def solve():
    """Index: 1991.
    Returns: the additional amount Sally needs to save for her trip.
    """
    # L1
    distance_to_sea_world = 165 # Sea World is 165 miles away
    round_trip_factor = 2 # WK
    total_driving_miles = round_trip_factor * distance_to_sea_world

    # L2
    miles_per_gallon = 30 # her car gets 30 miles per gallon of gas
    gallons_needed = total_driving_miles / miles_per_gallon

    # L3
    gas_cost_per_gallon = 3 # gas costs $3 a gallon
    total_gas_cost = gallons_needed * gas_cost_per_gallon

    # L4
    parking_cost = 10 # $10 to park
    park_entry_cost = 55 # $55 to get into the park
    meal_pass_cost = 25 # $25 for a meal pass
    total_trip_cost = parking_cost + park_entry_cost + meal_pass_cost + total_gas_cost

    # L5
    saved_money = 28 # She already has $28 saved
    amount_to_save_more = total_trip_cost - saved_money

    # FA
    answer = amount_to_save_more
    return answer