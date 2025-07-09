def solve(
    num_floors: int = 10, # The hotel has 10 floors
    rooms_per_floor: int = 10, # with 10 identical rooms on each floor
    unavailable_floors: int = 1 # the last floor is unavailable for the guests
):
    """Index: 84.
    Returns: the number of different rooms Hans could be checked into.
    """

    #: L1
    total_rooms = num_floors * rooms_per_floor # eval: 100 = 10 * 10

    #: L2
    available_rooms = total_rooms + (rooms_per_floor * unavailable_floors) # eval: 110 = 100 + (10 * 1)

    #: FA
    answer = available_rooms
    return answer # eval: return 110
