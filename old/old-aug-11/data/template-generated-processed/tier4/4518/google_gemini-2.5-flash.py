def solve():
    """Index: 4518.
    Returns: the total amount Carl will need to spend on gas.
    """
    # L1
    city_miles_one_way = 60 # 60 city miles
    round_trip_factor = 2 # WK
    city_miles_round_trip = city_miles_one_way * round_trip_factor

    # L2
    highway_miles_one_way = 200 # 200 highway miles
    highway_miles_round_trip = highway_miles_one_way * round_trip_factor

    # L3
    car_city_mpg = 30 # 30 miles per gallon in cities
    gallons_city = city_miles_round_trip / car_city_mpg

    # L4
    car_highway_mpg = 40 # 40 miles per gallon on the highway
    gallons_highway = highway_miles_round_trip / car_highway_mpg

    # L5
    total_gallons_needed = gallons_highway + gallons_city

    # L6
    gas_cost_per_gallon_display = 3.00 # $3.00 per gallon
    gas_cost_per_gallon_value = 3 # derived from calculator annotation
    total_spending = total_gallons_needed * gas_cost_per_gallon_value

    # FA
    answer = total_spending
    return answer