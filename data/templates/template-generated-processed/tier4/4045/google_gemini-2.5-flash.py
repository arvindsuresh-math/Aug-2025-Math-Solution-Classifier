def solve():
    """Index: 4045.
    Returns: the percentage of the total time Laura spent in the park.
    """
    # L1
    hours_per_trip_park = 2 # spent 2 hours at the park
    num_trips = 6 # six trips to park
    total_hours_in_park = hours_per_trip_park * num_trips

    # L2
    minutes_walk_per_trip = 30 # 30 minutes walking to and from the park
    hours_walk_per_trip = 0.5 # 0.5 of an hour walking to and from the park
    total_hours_walking = hours_walk_per_trip * num_trips

    # L3
    total_time_all_trips = total_hours_in_park + total_hours_walking

    # L4
    fraction_time_in_park = total_hours_in_park / total_time_all_trips

    # L5
    percent_multiplier = 100 # WK
    percentage_time_in_park = fraction_time_in_park * percent_multiplier

    # FA
    answer = percentage_time_in_park
    return answer