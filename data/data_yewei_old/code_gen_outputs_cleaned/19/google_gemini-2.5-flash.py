def solve_19():
    # Distance to work (one way)
    distance_to_work = 20 # miles
    # Number of workdays
    num_workdays = 5
    # Weekend bike ride distance
    weekend_ride_distance = 200 # miles
    # Biking speed
    bike_speed = 25 # mph

    # L1: Calculate daily commute distance (back and forth)
    daily_commute_distance = distance_to_work * 2

    # L2: Calculate total work biking distance for the week
    total_work_biking_distance = daily_commute_distance * num_workdays

    # L3: Calculate total biking distance for the week (work + weekend)
    total_weekly_biking_distance = total_work_biking_distance + weekend_ride_distance

    # L4: Calculate total time spent biking in hours
    total_biking_time_hours = total_weekly_biking_distance / bike_speed

    return total_biking_time_hours

# Execute the function to get the final answer
final_answer = solve_19()
print(final_answer)