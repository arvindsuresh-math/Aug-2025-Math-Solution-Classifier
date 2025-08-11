def solve():
    """Index: 7187.
    Returns: the number of cookies in the jar.
    """
    # L7
    removed_cookies_count = 1 # Taking 1 cookie away
    added_cookies_count = 5 # if 5 were added
    half_factor = 2 # half as many
    # The problem states: C - removed_cookies_count = (C + added_cookies_count) / half_factor
    # Solving for C:
    # 2 * (C - removed_cookies_count) = C + added_cookies_count
    # 2C - 2 * removed_cookies_count = C + added_cookies_count
    # 2C - C = added_cookies_count + 2 * removed_cookies_count
    # C = added_cookies_count + 2 * removed_cookies_count
    num_cookies = added_cookies_count + half_factor * removed_cookies_count

    # FA
    answer = num_cookies
    return answer