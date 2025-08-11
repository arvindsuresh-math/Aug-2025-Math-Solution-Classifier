def solve():
    """Index: 324.
    Returns: the total amount of money Legacy makes from cleaning all the floors.
    """
    # L1
    num_floors = 4 # four floors
    rooms_per_floor = 10 # ten rooms each
    total_rooms = num_floors * rooms_per_floor

    # L2
    hours_per_room = 6 # 6 hours to clean one room
    total_hours_cleaning = total_rooms * hours_per_room

    # L3
    hourly_rate = 15 # $15 per hour of work
    total_earnings = hourly_rate * total_hours_cleaning

    # FA
    answer = total_earnings
    return answer