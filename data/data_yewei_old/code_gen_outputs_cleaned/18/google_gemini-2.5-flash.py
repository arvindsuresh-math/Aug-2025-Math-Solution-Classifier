def solve():
    # Time taken to walk to work (one way)
    walk_time_one_way = 2  # hours

    # Number of times Roque walks to work per week
    walk_days_per_week = 3

    # Time taken to bike to work (one way)
    bike_time_one_way = 1  # hour

    # Number of times Roque bikes to work per week
    bike_days_per_week = 2

    # Calculate total walking time to work per week
    total_walk_to_work_time = walk_time_one_way * walk_days_per_week

    # Calculate total walking time to and from work per week (round trip)
    total_walk_commute_time = total_walk_to_work_time * 2

    # Calculate total biking time to work per week
    total_bike_to_work_time = bike_time_one_way * bike_days_per_week

    # Calculate total biking time to and from work per week (round trip)
    total_bike_commute_time = total_bike_to_work_time * 2

    # Calculate total commute time for the week
    total_commute_time_per_week = total_walk_commute_time + total_bike_commute_time

    return total_commute_time_per_week

# Execute the function to get the answer
answer = solve()