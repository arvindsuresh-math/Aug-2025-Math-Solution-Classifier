def solve():
    """Index: 2162.
    Returns: the total number of gallons of gas used.
    """
    # L1
    highway_miles = 210 # drove 210 miles on highways
    highway_mpg = 35 # car gets 35 miles for each gallon of gas
    gallons_highway = highway_miles / highway_mpg

    # L2
    city_miles = 54 # 54 miles on city streets
    city_mpg = 18 # car gets 18 miles for each gallon
    gallons_city = city_miles / city_mpg

    # L3
    total_gallons = gallons_highway + gallons_city

    # FA
    answer = total_gallons
    return answer