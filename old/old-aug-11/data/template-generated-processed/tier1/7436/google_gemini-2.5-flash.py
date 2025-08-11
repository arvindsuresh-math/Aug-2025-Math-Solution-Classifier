def solve():
    """Index: 7436.
    Returns: the difference in area between the largest room and the smallest room.
    """
    # L1
    largest_room_width = 45 # 45 feet wide
    largest_room_length = 30 # 30 feet long
    area_largest_room = largest_room_width * largest_room_length

    # L2
    smallest_room_width = 15 # 15 feet wide
    smallest_room_length = 8 # 8 feet long
    area_smallest_room = smallest_room_width * smallest_room_length

    # L3
    difference_in_area = area_largest_room - area_smallest_room

    # FA
    answer = difference_in_area
    return answer