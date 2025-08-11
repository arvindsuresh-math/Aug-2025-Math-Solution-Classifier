def solve():
    """Index: 4853.
    Returns: the total number of vehicles in all the lanes.
    """
    # L1
    num_lanes = 4 # four lanes
    trucks_per_lane = 60 # 60 trucks in each lane
    total_trucks = trucks_per_lane * num_lanes

    # L2
    multiplier_cars = 2 # twice as many
    cars_per_lane = multiplier_cars * total_trucks

    # L3
    total_cars = cars_per_lane * num_lanes

    # L4
    total_vehicles = total_trucks + total_cars

    # FA
    answer = total_vehicles
    return answer