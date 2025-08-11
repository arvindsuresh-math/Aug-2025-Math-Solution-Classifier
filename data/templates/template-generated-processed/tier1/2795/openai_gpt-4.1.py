def solve():
    """Index: 2795.
    Returns: the square footage of the new home office/personal gym room.
    """
    # L1
    bedroom_sqft = 309 # Holden's current master bedroom is 309 sq ft
    bathroom_sqft = 150 # his master bath is 150 sq ft
    combined_sqft = bedroom_sqft + bathroom_sqft

    # L2
    multiplier = 2 # twice as large as his bedroom and bathroom
    new_room_sqft = multiplier * combined_sqft

    # FA
    answer = new_room_sqft
    return answer