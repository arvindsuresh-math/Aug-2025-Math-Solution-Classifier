def solve():
    """Index: 5446.
    Returns: the total time in minutes to get to the 10th floor.
    """
    # L1
    num_even_floors = 5 # even-numbered floors (2, 4, 6, 8, 10)
    time_per_even_floor = 15 # 15 seconds to go up the stairs to the even-numbered floors
    total_time_even_floors = num_even_floors * time_per_even_floor

    # L2
    num_odd_floors = 5 # odd-numbered floors (1, 3, 5, 7, 9)
    time_per_odd_floor = 9 # 9 seconds to go up to the odd-numbered floors
    total_time_odd_floors = num_odd_floors * time_per_odd_floor

    # L3
    total_time_seconds = total_time_even_floors + total_time_odd_floors

    # L4
    seconds_per_minute = 60 # WK
    total_time_minutes = total_time_seconds / seconds_per_minute

    # FA
    answer = total_time_minutes
    return answer