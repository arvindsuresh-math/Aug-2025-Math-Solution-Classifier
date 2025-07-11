def solve():
    """Index: 1239.
    Returns: the total cost to replace the floor in Tom's room.
    """
    # L1
    room_length = 8 # Tom's room is 8*7 feet
    room_width = 7 # Tom's room is 8*7 feet
    room_area = room_length * room_width

    # L2
    new_floor_cost_per_sqft = 1.25 # new floor costs $1.25 per square foot
    new_floor_cost = room_area * new_floor_cost_per_sqft

    # L3
    removal_cost = 50 # cost $50 to remove the floor
    total_cost = removal_cost + new_floor_cost

    # FA
    answer = total_cost
    return answer