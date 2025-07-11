def solve():
    """Index: 1239.
    Returns: the total cost to replace the floor.
    """
    # L1
    room_length = 8 # 8*7 feet
    room_width = 7 # 8*7 feet
    room_area = room_length * room_width

    # L2
    cost_per_square_foot = 1.25 # $1.25 per square foot
    new_floor_cost = room_area * cost_per_square_foot

    # L3
    removal_cost = 50 # $50 to remove the floor
    total_cost = removal_cost + new_floor_cost

    # FA
    answer = total_cost
    return answer