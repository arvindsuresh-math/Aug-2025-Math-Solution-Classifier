def solve():
    """Index: 3018.
    Returns: the total ounces of water Kara drank with her medication over two weeks.
    """
    # L1
    ounces_per_tablet = 4 # 4 ounces of water
    tablets_per_day = 3 # take one tablet three times a day
    ounces_per_day = ounces_per_tablet * tablets_per_day

    # L2
    days_per_week = 7 # WK
    ounces_per_week = ounces_per_day * days_per_week

    # L3
    num_weeks = 2 # over those two weeks
    ounces_per_two_weeks_initial = ounces_per_week * num_weeks

    # L4
    forgotten_tablets = 2 # forgot twice on one day
    forgotten_ounces = forgotten_tablets * ounces_per_tablet

    # L5
    total_ounces_drank = ounces_per_two_weeks_initial - forgotten_ounces

    # FA
    answer = total_ounces_drank
    return answer