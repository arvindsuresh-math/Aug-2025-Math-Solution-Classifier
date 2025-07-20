def solve():
    """Index: 3208.
    Returns: the total number of pencils Sarah has.
    """
    # L1
    pencils_monday = 20 # 20 pencils on Monday
    pencils_tuesday = 18 # 18 more pencils on Tuesday
    pencils_after_monday_tuesday = pencils_monday + pencils_tuesday

    # L2
    multiplier_wednesday = 3 # triple the number of pencils she did on Tuesday
    pencils_wednesday = multiplier_wednesday * pencils_tuesday

    # L3
    total_pencils = pencils_after_monday_tuesday + pencils_wednesday

    # FA
    answer = total_pencils
    return answer