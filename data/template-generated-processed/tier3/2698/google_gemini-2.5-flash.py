def solve():
    """Index: 2698.
    Returns: the number of walls each person should paint.
    """
    # L1
    rooms_group1 = 5 # 5 of the rooms
    walls_per_room_group1 = 4 # have 4 walls each
    walls_group1 = rooms_group1 * walls_per_room_group1

    # L2
    rooms_group2 = 4 # The other 4 rooms
    walls_per_room_group2 = 5 # each have 5 walls each
    walls_group2 = rooms_group2 * walls_per_room_group2

    # L3
    total_walls = walls_group1 + walls_group2

    # L4
    num_people = 5 # 5 people in Amanda's family
    walls_per_person = total_walls / num_people

    # FA
    answer = walls_per_person
    return answer