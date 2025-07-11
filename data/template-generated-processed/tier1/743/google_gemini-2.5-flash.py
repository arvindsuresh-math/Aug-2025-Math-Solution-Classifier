def solve():
    """Index: 743.
    Returns: the total amount of fuel needed for the trip.
    """
    # L1
    num_passengers = 30 # 30 passengers
    num_flight_crew = 5 # 5 flight crew
    total_people = num_passengers + num_flight_crew

    # L2
    bags_per_person = 2 # each person brought two bags
    total_bags = total_people * bags_per_person

    # L3
    fuel_increase_per_person = 3 # 3 gallons per mile
    fuel_increase_from_people = total_people * fuel_increase_per_person

    # L4
    fuel_increase_per_bag = 2 # 2 gallons per mile
    fuel_increase_from_bags = total_bags * fuel_increase_per_bag

    # L5
    base_fuel_per_mile = 20 # 20 gallons of fuel per mile
    total_fuel_per_mile = fuel_increase_from_bags + fuel_increase_from_people + base_fuel_per_mile

    # L6
    trip_distance_miles = 400 # 400-mile trip
    total_fuel_needed = total_fuel_per_mile * trip_distance_miles

    # FA
    answer = total_fuel_needed
    return answer