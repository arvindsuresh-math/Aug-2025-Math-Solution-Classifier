def solve():
    """Index: 7211.
    Returns: the number of days it will take Cary to strip all the ivy off.
    """
    # L1
    removed_per_day = 6 # She strips 6 feet of ivy every day
    grows_per_night = 2 # the ivy grows another 2 feet every night
    net_removal_per_day = removed_per_day - grows_per_night

    # L2
    total_ivy = 40 # the tree is covered by 40 feet of ivy
    days_to_strip_ivy = total_ivy / net_removal_per_day

    # FA
    answer = days_to_strip_ivy
    return answer