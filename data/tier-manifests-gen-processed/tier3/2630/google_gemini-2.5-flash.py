def solve():
    """Index: 2630.
    Returns: the total duration of the road trip in hours.
    """
    # L1
    total_trip_hours = 14 # Carter has a 14-hour road trip
    stop_interval_hours = 2 # stop every 2 hours
    interval_stops = total_trip_hours / stop_interval_hours

    # L2
    food_stops = 2 # 2 additional stops for food
    gas_stops = 3 # 3 additional stops for gas
    total_pit_stops = interval_stops + food_stops + gas_stops

    # L3
    minutes_per_stop = 20 # each pit stop takes 20 minutes
    total_stop_minutes = minutes_per_stop * total_pit_stops

    # L4
    minutes_per_hour = 60 # WK
    additional_hours = total_stop_minutes / minutes_per_hour

    # L5
    final_trip_hours = total_trip_hours + additional_hours

    # FA
    answer = final_trip_hours
    return answer