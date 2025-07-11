def solve():
    """Index: 2296.
    Returns: the total combined square feet in all gardens.
    """
    # L1
    num_mancino_gardens = 3 # 3 gardens
    mancino_length = 16 # 16 feet
    mancino_width = 5 # 5 feet
    mancino_total_area = num_mancino_gardens * (mancino_length * mancino_width)

    # L2
    num_marquita_gardens = 2 # two gardens
    marquita_length = 8 # 8 feet
    marquita_width = 4 # 4 feet
    marquita_total_area = num_marquita_gardens * (marquita_length * marquita_width)

    # L3
    combined_total_area = mancino_total_area + marquita_total_area

    # FA
    answer = combined_total_area
    return answer