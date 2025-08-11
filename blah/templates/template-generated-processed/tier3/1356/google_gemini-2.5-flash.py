from fractions import Fraction

def solve():
    """Index: 1356.
    Returns: the total number of walls painted purple.
    """
    # L1
    total_rooms = 10 # a ten-bedroom house
    green_fraction = Fraction(3, 5) # 3/5 of the rooms
    green_rooms = green_fraction * total_rooms

    # L2
    purple_rooms = total_rooms - green_rooms

    # L3
    walls_per_room = 8 # 8 walls in each room
    purple_walls = walls_per_room * purple_rooms

    # FA
    answer = purple_walls
    return answer