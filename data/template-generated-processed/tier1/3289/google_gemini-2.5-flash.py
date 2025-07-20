def solve():
    """Index: 3289.
    Returns: the total number of rooms in the hotel.
    """
    # L1
    rooms_per_hall_wing1 = 32 # 32 rooms
    halls_per_floor_wing1 = 6 # 6 halls
    rooms_per_floor_wing1 = rooms_per_hall_wing1 * halls_per_floor_wing1

    # L2
    floors_wing1 = 9 # 9 floors
    total_rooms_wing1 = rooms_per_floor_wing1 * floors_wing1

    # L3
    rooms_per_hall_wing2 = 40 # 40 rooms
    halls_per_floor_wing2 = 9 # 9 halls
    rooms_per_floor_wing2 = rooms_per_hall_wing2 * halls_per_floor_wing2

    # L4
    floors_wing2 = 7 # 7 floors
    total_rooms_wing2 = rooms_per_floor_wing2 * floors_wing2

    # L5
    total_rooms_hotel = total_rooms_wing1 + total_rooms_wing2

    # FA
    answer = total_rooms_hotel
    return answer