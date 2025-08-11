def solve():
    """Index: 2793.
    Returns: the total number of cookies Lara is baking.
    """
    # L1
    rows_per_tray = 5 # five rows of cookies on a baking tray
    cookies_per_row = 6 # six cookies in one row
    cookies_per_tray = rows_per_tray * cookies_per_row

    # L2
    num_trays = 4 # four baking trays
    total_cookies = cookies_per_tray * num_trays

    # FA
    answer = total_cookies
    return answer