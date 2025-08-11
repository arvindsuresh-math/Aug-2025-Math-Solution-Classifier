def solve():
    """Index: 5942.
    Returns: the number of pencils Tim has.
    """
    # L1
    tyrah_pencils = 12 # If Tyrah has 12 pencils
    tyrah_multiplier = 6 # six times as many pencils as Sarah
    sarah_pencils = tyrah_pencils / tyrah_multiplier

    # L2
    tim_multiplier = 8 # eight times as many pencils as Sarah
    tim_pencils = tim_multiplier * sarah_pencils

    # FA
    answer = tim_pencils
    return answer