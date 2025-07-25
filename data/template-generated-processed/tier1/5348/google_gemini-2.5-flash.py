def solve():
    """Index: 5348.
    Returns: the area of the room in square inches.
    """
    # L1
    room_length_feet = 10 # 10 feet long in each direction
    inches_per_foot = 12 # 12 inches to a foot
    room_length_inches = room_length_feet * inches_per_foot

    # L2
    area_square_inches = room_length_inches * room_length_inches

    # FA
    answer = area_square_inches
    return answer