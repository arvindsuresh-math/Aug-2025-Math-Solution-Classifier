def solve():
    """Index: 982.
    Returns: the number of cookies left when Ted leaves.
    """
    # L1
    trays_per_day = 2 # two trays of cookies per day
    cookies_per_tray = 12 # each tray makes 12 cookies
    cookies_per_day = trays_per_day * cookies_per_tray

    # L2
    num_days = 6 # for 6 days
    total_cookies = cookies_per_day * num_days

    # L3
    frank_eats_per_day = 1 # Frank eats one cookie each day
    frank_total_eats = frank_eats_per_day * num_days

    # L4
    ted_eats = 4 # Ted eats 4 cookies
    cookies_left = total_cookies - frank_total_eats - ted_eats

    # FA
    answer = cookies_left
    return answer