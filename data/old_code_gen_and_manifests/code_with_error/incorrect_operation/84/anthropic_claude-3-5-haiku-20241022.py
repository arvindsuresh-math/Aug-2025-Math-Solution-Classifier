def solve(
    total_floors: int = 10,  # The hotel has 10 floors
    rooms_per_floor: int = 10,  # 10 identical rooms on each floor
    unavailable_floors: int = 1  # One floor is unavailable
):
    """Index: 84.
    Returns: the number of available rooms in the hotel."""

    #: L1
    total_rooms = total_floors - rooms_per_floor

    #: L2
    available_rooms = total_rooms - (unavailable_floors * rooms_per_floor)

    #: FA
    answer = available_rooms
    return answer