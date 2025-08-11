def solve():
    """Index: 5425.
    Returns: the number of fewer pounds of carbon emitted per year.
    """
    # L1
    initial_population = 80 # population is 80
    car_pollution_per_year = 10 # Each car on a road pollutes 10 pounds of carbon a year
    initial_total_emission = initial_population * car_pollution_per_year

    # L2
    bus_riders_percentage = 0.25 # 25% of the people who used to drive now take the bus
    num_bus_riders = initial_population * bus_riders_percentage

    # L3
    num_drivers_remaining = initial_population - num_bus_riders

    # L4
    emission_from_drivers = num_drivers_remaining * car_pollution_per_year

    # L5
    bus_pollution_per_year = 100 # A single bus pollutes 100 pounds of carbon a year
    new_total_emission = bus_pollution_per_year + emission_from_drivers

    # L6
    carbon_reduction = initial_total_emission - new_total_emission

    # FA
    answer = carbon_reduction
    return answer