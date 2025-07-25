def solve():
    """Index: 5428.
    Returns: the distance between the house and the market.
    """
    # L1
    distance_house_to_school = 50 # 50 meters from his house to school
    distance_round_trip_house_school = distance_house_to_school + distance_house_to_school

    # L2
    total_distance_walked = 140 # walks 140 meters in total
    distance_house_to_market = total_distance_walked - distance_round_trip_house_school

    # FA
    answer = distance_house_to_market
    return answer