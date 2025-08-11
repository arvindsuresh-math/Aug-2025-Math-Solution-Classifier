def solve():
    """Index: 757.
    Returns: the number of cups of kibble remaining in the bag.
    """
    # L1
    mary_morning_feed = 1 # 1 cup of kibble in the morning
    mary_evening_feed = 1 # 1 cup of kibble in the evening
    mary_total_feed = mary_morning_feed + mary_evening_feed

    # L2
    frank_afternoon_feed = 1 # 1 cup of kibble in the afternoon
    # "twice as much in the late evening as he had given Luna in the afternoon"
    frank_late_evening_feed = frank_afternoon_feed * 2
    frank_total_feed = frank_afternoon_feed + frank_late_evening_feed

    # L3
    total_fed = mary_total_feed + frank_total_feed

    # L4
    initial_bag_size = 12 # new, 12-cup bag of kibble
    remaining_kibble = initial_bag_size - total_fed

    # FA
    answer = remaining_kibble
    return answer