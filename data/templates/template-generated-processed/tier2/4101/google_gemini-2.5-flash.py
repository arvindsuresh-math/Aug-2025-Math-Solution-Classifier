def solve():
    """Index: 4101.
    Returns: the total distance, in land miles, that Buffy will travel.
    """
    # L1
    duration_one_sail = 4 # for 4 hours with one sail
    speed_one_sail = 25 # speed of 25 knots
    distance_one_sail = duration_one_sail * speed_one_sail

    # L2
    duration_two_sails = 4 # for another 4 hours with two sails
    speed_two_sails = 50 # speed of 50 knots
    distance_two_sails = duration_two_sails * speed_two_sails

    # L3
    total_nautical_miles = distance_one_sail + distance_two_sails

    # L4
    nautical_to_land_mile_conversion = 1.15 # one nautical mile equals 1.15 land miles
    total_land_miles = total_nautical_miles * nautical_to_land_mile_conversion

    # FA
    answer = total_land_miles
    return answer