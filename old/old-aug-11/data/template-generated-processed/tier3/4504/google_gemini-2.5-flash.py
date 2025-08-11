def solve():
    """Index: 4504.
    Returns: the total miles the car can drive in 13 hours.
    """
    # L1
    miles_per_hour = 8 # 8 miles in one hour
    initial_driving_hours = 5 # After 5 hours of constant driving
    miles_in_initial_driving = miles_per_hour * initial_driving_hours

    # L2
    pause_duration = 1 # takes 1 hour
    cycle_duration = initial_driving_hours + pause_duration

    # L3
    total_time = 13 # in 13 hours
    num_full_cycles = total_time // cycle_duration
    remaining_hours_after_cycles = total_time % cycle_duration

    # L4
    duration_of_full_cycles = num_full_cycles * cycle_duration

    # L5
    miles_driven_in_full_cycles = miles_in_initial_driving * num_full_cycles

    # L6
    remaining_driving_time_from_total = total_time - duration_of_full_cycles

    # L7
    total_miles_driven = miles_driven_in_full_cycles + miles_per_hour

    # FA
    answer = total_miles_driven
    return answer