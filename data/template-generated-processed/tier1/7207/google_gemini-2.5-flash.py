def solve():
    """Index: 7207.
    Returns: the number of years in the future until the specified anniversary.
    """
    # L1
    anniversary_target = 200 # 200th anniversary
    years_before_anniversary = 5 # 5 years before its 200th anniversary
    target_years_from_built = anniversary_target - years_before_anniversary

    # L2
    years_ago_built = 100 # built 100 years ago
    years_in_future = target_years_from_built - years_ago_built

    # FA
    answer = years_in_future
    return answer