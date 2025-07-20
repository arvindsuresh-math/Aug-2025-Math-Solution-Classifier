def solve():
    """Index: 6900.
    Returns: the total number of glass panels in the whole house.
    """
    # L1
    double_windows_downstairs = 6 # 6 double windows downstairs
    windows_per_double = 2 # WK
    windows_downstairs = double_windows_downstairs * windows_per_double

    # L2
    single_windows_upstairs = 8 # 8 single windows upstairs
    total_windows = windows_downstairs + single_windows_upstairs

    # L3
    panels_per_window = 4 # 4 glass panels each
    total_glass_panels = total_windows * panels_per_window

    # FA
    answer = total_glass_panels
    return answer