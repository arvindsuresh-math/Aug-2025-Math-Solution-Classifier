def solve():
    """Index: 657.
    Returns: the time Pete should leave.
    """
    # L1
    minutes_per_hour = 60 # WK
    train_duration_hours = 1 # 1hr 20-minute train
    train_duration_minutes_part = 20 # 1hr 20-minute train
    train_duration_total_minutes = (train_duration_hours * minutes_per_hour) + train_duration_minutes_part

    # L2
    walk_duration_minutes = 10 # 10-minute walk
    total_travel_minutes = train_duration_total_minutes + walk_duration_minutes

    # L3
    travel_hours = total_travel_minutes // minutes_per_hour
    travel_remaining_minutes = total_travel_minutes % minutes_per_hour

    # L4
    arrival_time_hours = 9 # 0900 hours
    arrival_time_minutes = 0 # 0900 hours
    
    arrival_total_minutes = arrival_time_hours * minutes_per_hour + arrival_time_minutes
    travel_duration_total_minutes_calc = travel_hours * minutes_per_hour + travel_remaining_minutes
    departure_total_minutes = arrival_total_minutes - travel_duration_total_minutes_calc
    
    departure_hours = departure_total_minutes // minutes_per_hour
    departure_minutes = departure_total_minutes % minutes_per_hour
    
    travel_duration_display = f"{travel_hours:02d}{travel_remaining_minutes:02d}"
    arrival_time_display = f"{arrival_time_hours:02d}{arrival_time_minutes:02d}"
    departure_time_display = f"{departure_hours:02d}{departure_minutes:02d}"

    # FA
    answer = departure_time_display
    return answer