def solve():
    """Index: 6938.
    Returns: the total minutes to deliver all cars.
    """
    # L1
    initial_coal_cars = 6 # 6 coal cars
    coal_cars_per_station = 2 # up to 2 coal cars
    stations_for_coal = initial_coal_cars / coal_cars_per_station

    # L2
    initial_iron_cars = 12 # 12 iron cars
    iron_cars_per_station = 3 # 3 iron cars
    stations_for_iron = initial_iron_cars / iron_cars_per_station

    # L3
    initial_wood_cars = 2 # 2 wood cars
    wood_cars_per_station = 1 # 1 wood car
    stations_for_wood = initial_wood_cars / wood_cars_per_station

    # L4
    max_stations_needed = max(stations_for_coal, stations_for_iron, stations_for_wood)
    minutes_per_station_travel = 25 # 25 minutes to travel between them
    total_minutes_needed = max_stations_needed * minutes_per_station_travel

    # FA
    answer = total_minutes_needed
    return answer