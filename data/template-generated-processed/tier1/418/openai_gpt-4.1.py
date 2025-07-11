def solve():
    """Index: 418.
    Returns: the number of pencils Ken kept.
    """
    # L1
    manny_pencils = 10 # Ken gave ten pencils to Manny
    nilo_more_than_manny = 10 # ten more pencils to Nilo than he gave to Manny
    nilo_pencils = manny_pencils + nilo_more_than_manny

    # L2
    total_given = manny_pencils + nilo_pencils

    # L3
    ken_initial = 50 # Ken had fifty pencils
    ken_kept = ken_initial - total_given

    # FA
    answer = ken_kept
    return answer