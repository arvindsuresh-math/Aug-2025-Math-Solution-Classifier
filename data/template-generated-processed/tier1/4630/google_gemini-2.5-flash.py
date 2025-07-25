def solve():
    """Index: 4630.
    Returns: the total time in minutes to complete all runway trips.
    """
    # L1
    num_models = 6 # 6 models in the show
    bathing_suit_sets_per_model = 2 # two sets of bathing suits
    bathing_suit_trips = num_models * bathing_suit_sets_per_model

    # L2
    evening_wear_sets_per_model = 3 # three sets of evening wear clothing
    evening_wear_trips = num_models * evening_wear_sets_per_model

    # L3
    total_trips = bathing_suit_trips + evening_wear_trips

    # L4
    minutes_per_trip = 2 # 2 minutes to walk out to the end of the runway and back
    total_time_minutes = total_trips * minutes_per_trip

    # FA
    answer = total_time_minutes
    return answer