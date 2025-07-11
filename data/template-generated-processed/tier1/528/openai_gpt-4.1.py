def solve():
    """Index: 528.
    Returns: the total amount James paid for everything.
    """
    # L1
    num_dirtbikes = 3 # 3 dirt bikes
    price_per_dirtbike = 150 # $150 each
    dirtbike_cost = num_dirtbikes * price_per_dirtbike

    # L2
    price_per_offroad = 300 # $300 each
    num_offroad = 4 # 4 off-road vehicles
    offroad_cost = price_per_offroad * num_offroad

    # L3
    total_vehicles = num_dirtbikes + num_offroad

    # L4
    registration_per_vehicle = 25 # $25 to register each
    registration_cost = registration_per_vehicle * total_vehicles

    # L5
    total_cost = dirtbike_cost + offroad_cost + registration_cost

    # FA
    answer = total_cost
    return answer