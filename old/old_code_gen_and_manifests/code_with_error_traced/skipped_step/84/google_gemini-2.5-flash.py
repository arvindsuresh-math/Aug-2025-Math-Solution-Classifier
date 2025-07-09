def solve(
        num_floors: int = 10, # The hotel has 10 floors
        rooms_per_floor: int = 10, # with 10 identical rooms on each floor
        unavailable_floors: int = 1 # the last floor is unavailable
    ):
    """Index: 84.
    Returns: the number of different rooms Hans could be checked into.
    """

    #: L1

    #: L2
    available_rooms = rooms_per_floor - (unavailable_floors * rooms_per_floor) # eval: 0 = 10 - (1 * 10)

    #: FA
    answer = available_rooms
    return answer # eval: return 0
