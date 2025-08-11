def solve():
    """Index: 5227.
    Returns: the number of more legos Julian needs.
    """
    # L1
    legos_per_airplane = 240 # 240 legos
    num_airplanes = 2 # two identical airplanes
    total_legos_needed = legos_per_airplane * num_airplanes

    # L2
    julian_has_legos = 400 # 400 legos
    legos_needed_more = total_legos_needed - julian_has_legos

    # FA
    answer = legos_needed_more
    return answer