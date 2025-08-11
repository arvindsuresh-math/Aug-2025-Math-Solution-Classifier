def solve():
    """Index: 2256.
    Returns: the number of times Carson can ride the giant slide.
    """
    # L1
    carnival_hours = 4 # 4 hours at a carnival
    minutes_per_hour = 60 # WK
    total_carnival_minutes = carnival_hours * minutes_per_hour

    # L2
    roller_coaster_rides = 4 # rides the roller coaster 4 times
    roller_coaster_wait_time = 30 # wait for the roller coaster is 30 minutes
    total_roller_coaster_time = roller_coaster_rides * roller_coaster_wait_time

    # L3
    tilt_a_whirl_wait_time = 60 # wait for the tilt-a-whirl is 60 minutes
    remaining_time_after_rides = total_carnival_minutes - total_roller_coaster_time - tilt_a_whirl_wait_time

    # L4
    giant_slide_wait_time = 15 # wait for the giant slide is 15 minutes
    num_giant_slide_rides = remaining_time_after_rides / giant_slide_wait_time

    # FA
    answer = num_giant_slide_rides
    return answer