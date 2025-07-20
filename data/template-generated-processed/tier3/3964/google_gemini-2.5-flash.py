from fractions import Fraction

def solve():
    """Index: 3964.
    Returns: the number of people in the conference center.
    """
    # L1
    room_capacity = 80 # Each room can hold up to 80 people
    num_rooms = 6 # six rooms
    total_capacity = room_capacity * num_rooms

    # L2
    fullness_fraction = Fraction(2, 3) # only 2/3 full
    people_in_center = total_capacity * fullness_fraction

    # FA
    answer = people_in_center
    return answer