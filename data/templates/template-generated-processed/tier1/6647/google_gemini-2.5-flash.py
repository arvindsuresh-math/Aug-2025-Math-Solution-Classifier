def solve():
    """Index: 6647.
    Returns: the number of fewer cans collected today than yesterday.
    """
    # L1
    sarah_cans_yesterday = 50 # Sarah collected 50 aluminum cans
    lara_more_than_sarah_yesterday = 30 # Lara collected 30 more aluminum cans
    lara_cans_yesterday = sarah_cans_yesterday + lara_more_than_sarah_yesterday

    # L2
    total_cans_yesterday = sarah_cans_yesterday + lara_cans_yesterday

    # L3
    sarah_cans_today = 40 # Sarah collected 40
    lara_cans_today = 70 # Lara collected 70 aluminum cans
    total_cans_today = sarah_cans_today + lara_cans_today

    # L4
    fewer_cans_today = total_cans_yesterday - total_cans_today

    # FA
    answer = fewer_cans_today
    return answer