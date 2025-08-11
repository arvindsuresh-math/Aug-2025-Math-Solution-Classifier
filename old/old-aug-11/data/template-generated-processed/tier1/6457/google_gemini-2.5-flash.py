def solve():
    """Index: 6457.
    Returns: the total area of all rooms.
    """
    # L1
    initial_length = 13 # 13 feet
    length_increase = 2 # increases each dimension by 2 feet
    new_length = initial_length + length_increase

    # L2
    initial_width = 18 # 18 feet
    new_width = initial_width + length_increase

    # L3
    room_area = new_length * new_width

    # L4
    initial_room_count = 1 # James has a room
    additional_rooms = 3 # builds 3 more rooms
    total_equal_size_rooms = initial_room_count + additional_rooms

    # L5
    area_equal_size_rooms = total_equal_size_rooms * room_area

    # L6
    multiplier_for_twice_size = 2 # 1 room of twice that size
    area_twice_size_room = room_area * multiplier_for_twice_size

    # L7
    total_area = area_equal_size_rooms + area_twice_size_room

    # FA
    answer = total_area
    return answer