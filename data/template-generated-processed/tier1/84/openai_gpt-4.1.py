def solve():
    """Index: 84.
    Returns: the number of different rooms Hans could be checked in.
    """
    # L1
    num_floors = 10 # 10 floors
    rooms_per_floor = 10 # 10 identical rooms on each floor
    total_rooms = num_floors * rooms_per_floor

    # L2
    unavailable_floors = 1 # last floor is unavailable
    unavailable_rooms = unavailable_floors * rooms_per_floor
    available_rooms = total_rooms - unavailable_rooms

    # FA
    answer = available_rooms
    return answer