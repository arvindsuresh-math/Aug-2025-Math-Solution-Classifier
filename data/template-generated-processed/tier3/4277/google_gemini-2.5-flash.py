def solve():
    """Index: 4277.
    Returns: the total number of buildings required for the new city.
    """
    # L1
    pittsburg_stores = 2000 # 2000 stores
    stores_divisor = 2 # half the number of stores
    new_city_stores = pittsburg_stores / stores_divisor

    # L2
    hospitals_multiplier = 2 # twice as many hospitals
    pittsburg_hospitals = 500 # 500 hospitals
    new_city_hospitals = hospitals_multiplier * pittsburg_hospitals

    # L3
    pittsburg_schools = 200 # 200 schools
    schools_reduction = 50 # 50 fewer schools
    new_city_schools = pittsburg_schools - schools_reduction

    # L4
    pittsburg_police_stations = 20 # 20 police stations
    police_stations_addition = 5 # 5 more police stations
    new_city_police_stations = pittsburg_police_stations + police_stations_addition

    # L5
    total_buildings = new_city_stores + new_city_hospitals + new_city_schools + new_city_police_stations

    # FA
    answer = total_buildings
    return answer