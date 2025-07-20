def solve():
    """Index: 6800.
    Returns: the number of pencils Autumn had left.
    """
    # L1
    misplaced_pencils = 7 # misplaced 7 pencils
    broke_pencils = 3 # broke 3 pencils
    pencils_lost = misplaced_pencils + broke_pencils

    # L2
    found_pencils = 4 # found 4
    bought_pencils = 2 # bought 2
    pencils_gained = found_pencils + bought_pencils

    # L3
    initial_pencils = 20 # purchased a pack of 20 pencils
    pencils_left = initial_pencils - pencils_lost + pencils_gained

    # FA
    answer = pencils_left
    return answer