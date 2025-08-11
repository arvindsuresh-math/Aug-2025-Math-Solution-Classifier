def solve():
    """Index: 6142.
    Returns: the total amount Krystiana earns every month.
    """
    # L1
    cost_first_floor_room = 15 # rooms on the first floor cost $15 per month
    rooms_per_floor = 3 # each floor has 3 rooms
    earnings_first_floor = cost_first_floor_room * rooms_per_floor

    # L2
    cost_second_floor_room = 20 # rooms on the 2nd floor cost $20 per month
    earnings_second_floor = cost_second_floor_room * rooms_per_floor

    # L3
    multiplier_third_floor_cost = 2 # twice as much as the rooms on the first floor
    cost_third_floor_room = cost_first_floor_room * multiplier_third_floor_cost

    # L4
    occupied_third_floor_rooms = 2 # only two rooms are occupied
    earnings_third_floor = cost_third_floor_room * occupied_third_floor_rooms

    # L5
    total_earnings = earnings_second_floor + earnings_third_floor + earnings_first_floor

    # FA
    answer = total_earnings
    return answer