def solve():
    """Index: 982.
    Returns: the number of cookies left when Ted leaves.
    """
    # L1
    trays_per_day = 2 # two trays of cookies per day
    cookies_per_tray = 12 # each tray makes 12 cookies
    cookies_per_day = trays_per_day * cookies_per_tray

    # L2
    baking_days = 6 # for 6 days
    total_baked_cookies = cookies_per_day * baking_days

    # L3
    frank_eats_per_day = 1 # eats one cookie each day
    total_frank_eats = frank_eats_per_day * baking_days

    # L4
    ted_eats = 4 # eats 4 cookies
    cookies_left = total_baked_cookies - total_frank_eats - ted_eats

    # FA
    answer = cookies_left
    return answer