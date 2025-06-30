def solve(
    total_floors: int = 10,  # The hotel has 10 floors
    rooms_per_floor: int = 10,  # 10 identical rooms on each floor
    unavailable_floors: int = 1  # One floor is unavailable
):
    """Index: 84.
    Returns: the number of available rooms in the hotel."""
    #: L1
    total_rooms = total_floors * rooms_per_floor # eval: 100 = 10 * 10
    #: L2
    available_rooms = total_rooms - (unavailable_floors * rooms_per_floor) # eval: 90 = 100 - (1 * 10)
    answer = available_rooms  # FINAL ANSWER # eval: 90 = 90  # FINAL ANSWER
    return answer # eval: return 90