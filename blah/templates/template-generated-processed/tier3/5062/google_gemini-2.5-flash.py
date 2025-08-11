def solve():
    """Index: 5062.
    Returns: the number of rooms in the building that have 2 windows.
    """
    # L1
    rooms_with_4_windows = 5 # 5 rooms have 4 windows
    windows_per_4_window_room = 4 # 4 windows
    windows_from_4_window_rooms = windows_per_4_window_room * rooms_with_4_windows

    # L2
    rooms_with_3_windows = 8 # 8 rooms have 3 windows
    windows_per_3_window_room = 3 # 3 windows
    windows_from_3_window_rooms = rooms_with_3_windows * windows_per_3_window_room

    # L3
    total_windows = 122 # 122 windows total
    remaining_windows = total_windows - windows_from_4_window_rooms - windows_from_3_window_rooms

    # L4
    windows_per_2_window_room = 2 # have 2 windows
    rooms_with_2_windows = remaining_windows / windows_per_2_window_room

    # FA
    answer = rooms_with_2_windows
    return answer