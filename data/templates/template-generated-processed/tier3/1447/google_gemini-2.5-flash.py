def solve():
    """Index: 1447.
    Returns: the difference in trip duration between Ann and Mary.
    """
    # L1
    mary_distance = 630 # Mary slides down a hill that's 630 feet long
    mary_speed = 90 # at a speed of 90 feet/minute
    mary_time = mary_distance / mary_speed

    # L2
    ann_distance = 800 # Ann slides down a hill that's 800 feet long
    ann_speed = 40 # at a rate of 40 feet/minute
    ann_time = ann_distance / ann_speed

    # L3
    time_difference = ann_time - mary_time

    # FA
    answer = time_difference
    return answer