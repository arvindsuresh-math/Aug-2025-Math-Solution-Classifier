def solve():
    """Index: 3932.
    Returns: the number of rooms in Susie's house.
    """
    # L1
    total_hours = 2 # 2 hours
    minutes_per_hour = 60 # WK
    total_vacuuming_minutes = total_hours * minutes_per_hour

    # L2
    time_per_room = 20 # 20 minutes
    number_of_rooms = total_vacuuming_minutes / time_per_room

    # FA
    answer = number_of_rooms
    return answer