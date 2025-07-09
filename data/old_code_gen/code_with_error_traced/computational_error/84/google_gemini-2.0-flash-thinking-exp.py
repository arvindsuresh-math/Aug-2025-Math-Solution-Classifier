def solve(
    total_floors: int = 10, # The hotel has 10 floors
    rooms_per_floor: int = 10, # with 10 identical rooms on each floor
    unavailable_floors: int = 1 # the last floor is unavailable
):
    """Index: 84.
    Returns: the number of different rooms Hans could be checked into.
    """

    #: L1
    total_rooms = total_floors * rooms_per_floor # eval: 100 = 10 * 10

    #: L2
    unavailable_room_count = unavailable_floors * rooms_per_floor # eval: 10 = 1 * 10
    available_rooms = 91 # eval: 91 = 91

    #: FA
    answer = available_rooms
    return answer # eval: return 91
