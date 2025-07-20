def solve():
    """Index: 4791.
    Returns: the total time both animals sleep in one week.
    """
    # L1
    cougar_sleep_night = 4 # sleeping for 4 hours at night
    zebra_sleep_more = 2 # zebra for 2 hours more
    zebra_sleep_night = cougar_sleep_night + zebra_sleep_more

    # L2
    days_in_week = 7 # WK
    cougar_sleep_week = cougar_sleep_night * days_in_week

    # L3
    zebra_sleep_week = zebra_sleep_night * days_in_week

    # L4
    total_sleep_week = cougar_sleep_week + zebra_sleep_week

    # FA
    answer = total_sleep_week
    return answer