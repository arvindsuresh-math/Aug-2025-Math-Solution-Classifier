def solve():
    """Index: 7136.
    Returns: the total number of chips left uneaten.
    """
    # L1
    dozen = 12 # WK
    num_dozens = 4 # 4 dozen in total
    total_cookies = dozen * num_dozens

    # L2
    eaten_divisor = 2 # half the cookies
    remaining_cookies = total_cookies / eaten_divisor

    # L3
    chips_per_cookie = 7 # exactly 7 chips
    remaining_chips = remaining_cookies * chips_per_cookie

    # FA
    answer = remaining_chips
    return answer