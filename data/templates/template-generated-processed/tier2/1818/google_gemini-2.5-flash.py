def solve():
    """Index: 1818.
    Returns: the number of non-hot peppers Joel picked.
    """
    # L1
    peppers_sunday = 7 # picks 7 on Sunday
    peppers_monday = 12 # 12 on Monday
    peppers_tuesday = 14 # 14 on Tuesday
    peppers_wednesday = 12 # 12 on Wednesday
    peppers_thursday = 5 # 5 on Thursday
    peppers_friday = 18 # 18 on Friday
    peppers_saturday = 12 # 12 on Saturday
    total_peppers_picked = peppers_sunday + peppers_monday + peppers_tuesday + peppers_wednesday + peppers_thursday + peppers_friday + peppers_saturday

    # L2
    total_percent = 100 # WK
    hot_pepper_percent = 20 # 20% of the peppers are hot
    non_hot_pepper_percent = total_percent - hot_pepper_percent

    # L3
    non_hot_pepper_percent_decimal = 0.8 # from solution text: .8
    non_hot_peppers_count = total_peppers_picked * non_hot_pepper_percent_decimal

    # FA
    answer = non_hot_peppers_count
    return answer