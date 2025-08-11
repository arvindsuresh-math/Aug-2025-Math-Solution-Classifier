def solve():
    """Index: 4728.
    Returns: the total weight of onions harvested.
    """
    # L1
    bags_per_trip = 10 # ten bags per trip
    weight_per_bag_kg = 50 # 50 kgs bags
    weight_per_trip_kg = bags_per_trip * weight_per_bag_kg

    # L2
    num_trips = 20 # makes 20 trips
    total_weight_kg = num_trips * weight_per_trip_kg

    # FA
    answer = total_weight_kg
    return answer