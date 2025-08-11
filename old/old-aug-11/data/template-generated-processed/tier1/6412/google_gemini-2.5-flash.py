def solve():
    """Index: 6412.
    Returns: the total number of gingerbreads Diane bakes.
    """
    # L1
    num_trays_1 = 4 # four trays
    gingerbreads_per_tray_1 = 25 # 25 gingerbreads in each tray
    total_gingerbreads_tray1 = num_trays_1 * gingerbreads_per_tray_1

    # L2
    num_trays_2 = 3 # three trays
    gingerbreads_per_tray_2 = 20 # 20 gingerbreads in each tray
    total_gingerbreads_tray2 = num_trays_2 * gingerbreads_per_tray_2

    # L3
    total_gingerbreads_baked = total_gingerbreads_tray1 + total_gingerbreads_tray2

    # FA
    answer = total_gingerbreads_baked
    return answer