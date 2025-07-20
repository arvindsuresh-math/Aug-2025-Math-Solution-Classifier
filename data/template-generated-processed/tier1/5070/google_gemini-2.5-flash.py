def solve():
    """Index: 5070.
    Returns: the total number of people in the house.
    """
    # L1
    charlie = 1 # Charlie
    susan = 1 # his wife Susan
    initial_bedroom_people = charlie + susan

    # L2
    sarah_friends = 4 # 4 friends
    sarah = 1 # Sarah
    sarah_group = sarah_friends + sarah

    # L3
    total_bedroom_people = sarah_group + initial_bedroom_people

    # L4
    living_room_people = 8 # 8 people in the living room
    total_people_in_house = living_room_people + total_bedroom_people

    # FA
    answer = total_people_in_house
    return answer