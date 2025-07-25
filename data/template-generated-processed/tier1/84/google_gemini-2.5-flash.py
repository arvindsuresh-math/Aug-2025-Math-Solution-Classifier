def solve():
    """Index: 84.
    Returns: the number of different rooms Hans could be checked in.
    """
    # L1
    num_floors = 10 # 10 floors
    rooms_per_floor = 10 # 10 identical rooms on each floor
    total_rooms = num_floors * rooms_per_floor

    # L2
    # The problem states "the last floor is unavailable", implying 1 floor is unavailable.
    # Since each floor has 'rooms_per_floor' rooms, the number of unavailable rooms is 'rooms_per_floor'.
    available_rooms = total_rooms - rooms_per_floor

    # FA
    answer = available_rooms
    return answer