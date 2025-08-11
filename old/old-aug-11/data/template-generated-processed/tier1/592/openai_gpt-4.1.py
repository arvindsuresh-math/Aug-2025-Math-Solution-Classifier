def solve():
    """Index: 592.
    Returns: the total liters of fuel John should plan to use for both trips.
    """
    # L1
    first_trip_km = 30 # first trip of 30 km
    fuel_per_km = 5 # 5 liters of fuel per km
    first_trip_fuel = first_trip_km * fuel_per_km

    # L2
    second_trip_km = 20 # second trip of 20 km
    second_trip_fuel = second_trip_km * fuel_per_km

    # L3
    total_fuel = first_trip_fuel + second_trip_fuel

    # FA
    answer = total_fuel
    return answer