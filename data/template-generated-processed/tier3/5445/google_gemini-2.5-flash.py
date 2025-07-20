def solve():
    """Index: 5445.
    Returns: the number of gallons of gas Kennedy started with.
    """
    # L1
    distance_to_school = 15 # 15 miles to school
    distance_to_softball = 6 # 6 miles to the softball park
    distance_to_restaurant = 2 # 2 miles to a burger restaurant
    distance_to_friend = 4 # 4 miles to her friend’s house
    distance_home = 11 # 11 miles home
    total_miles_driven = distance_to_school + distance_to_softball + distance_to_restaurant + distance_to_friend + distance_home

    # L2
    miles_per_gallon = 19 # 19 miles per gallon of gas
    gallons_started_with = total_miles_driven / miles_per_gallon

    # FA
    answer = gallons_started_with
    return answer