def solve():
    """Index: 6136.
    Returns: the number of cookies Candy placed in each pack.
    """
    # L1
    num_trays = 4 # four trays
    cookies_per_tray = 24 # 24 cookies in each tray
    total_cookies = num_trays * cookies_per_tray

    # L2
    num_packs = 8 # eight packs
    cookies_per_pack = total_cookies / num_packs

    # FA
    answer = cookies_per_pack
    return answer