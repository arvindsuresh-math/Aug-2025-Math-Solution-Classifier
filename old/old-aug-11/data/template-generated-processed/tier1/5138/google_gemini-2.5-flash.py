def solve():
    """Index: 5138.
    Returns: the total number of towels the hotel hands out.
    """
    # L1
    num_rooms = 10 # 10 rooms
    people_per_room = 3 # family of 3
    total_people = num_rooms * people_per_room

    # L2
    towels_per_person = 2 # 2 towels
    total_towels = total_people * towels_per_person

    # FA
    answer = total_towels
    return answer