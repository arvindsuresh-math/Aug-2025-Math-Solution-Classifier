def solve():
    """Index: 4943.
    Returns: the number of half-gallons of milk needed to bake the specified number of cookies.
    """
    # L1
    initial_cookies = 40 # bake 40 cookies
    milk_for_initial_cookies = 10 # 10 half-gallons of milk
    cookies_per_half_gallon = initial_cookies / milk_for_initial_cookies

    # L2
    target_cookies = 200 # bake 200 cookies
    half_gallons_needed = target_cookies / cookies_per_half_gallon

    # FA
    answer = half_gallons_needed
    return answer