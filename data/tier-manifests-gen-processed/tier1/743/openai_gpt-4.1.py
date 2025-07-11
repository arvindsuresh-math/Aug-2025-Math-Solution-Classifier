def solve():
    """Index: 743.
    Returns: the total gallons of fuel needed for the 400-mile trip.
    """
    # L1
    num_passengers = 30 # 30 passengers
    num_crew = 5 # 5 flight crew
    total_people = num_passengers + num_crew

    # L2
    bags_per_person = 2 # each person brought two bags
    total_bags = total_people * bags_per_person

    # L3
    fuel_increase_per_person = 3 # increases this amount by 3 gallons per mile
    people_fuel_increase = total_people * fuel_increase_per_person

    # L4
    fuel_increase_per_bag = 2 # each bag increases it by 2 gallons per mile
    bags_fuel_increase = total_bags * fuel_increase_per_bag

    # L5
    base_fuel_per_mile = 20 # empty plane needs 20 gallons of fuel per mile
    total_fuel_per_mile = bags_fuel_increase + people_fuel_increase + base_fuel_per_mile

    # L6
    trip_miles = 400 # 400-mile trip
    total_fuel = total_fuel_per_mile * trip_miles

    # FA
    answer = total_fuel
    return answer