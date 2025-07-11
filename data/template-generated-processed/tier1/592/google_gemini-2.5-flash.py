def solve():
    """Index: 592.
    Returns: the total liters of fuel John should plan to use.
    """
    # L1
    fuel_per_km = 5 # 5 liters of fuel per km
    first_trip_distance = 30 # two trips of 30 km
    first_trip_fuel = first_trip_distance * fuel_per_km

    # L2
    second_trip_distance = 20 # and 20 km
    second_trip_fuel = second_trip_distance * fuel_per_km

    # L3
    total_fuel = first_trip_fuel + second_trip_fuel

    # FA
    answer = total_fuel
    return answer