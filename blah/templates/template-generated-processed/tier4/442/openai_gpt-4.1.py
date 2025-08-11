def solve():
    """Index: 442.
    Returns: the average percentage taller the cranes are than the buildings.
    """
    # L1
    building1_height = 200 # 200 feet tall building
    crane1_height = 228 # 228 feet tall crane
    percent1 = (crane1_height - building1_height) / building1_height * 100

    # L2
    building2_height = 100 # 100 feet tall building
    crane2_height = 120 # 120 feet tall crane
    percent2 = (crane2_height - building2_height) / building2_height * 100

    # L3
    building3_height = 140 # 140 feet tall building
    crane3_height = 147 # 147 feet tall crane
    percent3 = (crane3_height - building3_height) / building3_height * 100

    # L4
    total_percent = percent1 + percent2 + percent3

    # L5
    num_cranes = 3 # WK
    average_percent = total_percent / num_cranes

    # FA
    answer = average_percent
    return answer