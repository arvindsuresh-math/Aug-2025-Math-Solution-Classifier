def solve():
    """Index: 6758.
    Returns: the total hours needed to remove the remaining wallpaper.
    """
    # L1
    total_dining_room_walls = 4 # 4 walled dining room
    walls_removed_dining_room = 1 # 1 wall
    remaining_dining_room_walls = total_dining_room_walls - walls_removed_dining_room

    # L2
    total_living_room_walls = 4 # 4 walled living room
    total_remaining_walls = remaining_dining_room_walls + total_living_room_walls

    # L3
    hours_per_wall = 2 # 2 hours removing wallpaper from just 1 wall
    total_hours_needed = hours_per_wall * total_remaining_walls

    # FA
    answer = total_hours_needed
    return answer