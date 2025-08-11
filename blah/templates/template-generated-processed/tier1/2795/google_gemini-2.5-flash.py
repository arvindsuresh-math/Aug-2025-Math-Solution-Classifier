def solve():
    """Index: 2795.
    Returns: the square footage of the new room.
    """
    # L1
    bedroom_sq_ft = 309 # 309 sq ft
    bathroom_sq_ft = 150 # 150 sq ft
    total_bedroom_bathroom_sq_ft = bedroom_sq_ft + bathroom_sq_ft

    # L2
    multiplier_twice = 2 # twice as large
    new_room_sq_ft = multiplier_twice * total_bedroom_bathroom_sq_ft

    # FA
    answer = new_room_sq_ft
    return answer