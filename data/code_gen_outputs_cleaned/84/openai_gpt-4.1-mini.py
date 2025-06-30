def solve(
    total_floors: int = 10,  # The hotel has 10 floors
    rooms_per_floor: int = 10,  # 10 identical rooms on each floor
    unavailable_floors: int = 1  # The last floor is unavailable
):
    """Index: 84.
    Returns: the number of available rooms Hans could be checked into.
    """
    #: L1
    total_rooms = total_floors * rooms_per_floor

    #: L2
    available_rooms = total_rooms - (unavailable_floors * rooms_per_floor)

    answer = available_rooms  # FINAL ANSWER
    return answer