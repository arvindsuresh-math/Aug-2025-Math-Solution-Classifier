def solve():
    """Index: 5487.
    Returns: the total number of pencils Mitchell and Antonio have together.
    """
    # L1
    mitchell_pencils = 30 # Mitchell has 30 pencils
    more_than_antonio = 6 # 6 more pencils than Antonio
    antonio_pencils = mitchell_pencils - more_than_antonio

    # L2
    total_pencils = antonio_pencils + mitchell_pencils

    # FA
    answer = total_pencils
    return answer