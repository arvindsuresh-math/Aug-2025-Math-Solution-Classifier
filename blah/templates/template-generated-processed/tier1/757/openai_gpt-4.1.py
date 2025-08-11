def solve():
    """Index: 757.
    Returns: the number of cups of kibble remaining in the bag the next morning.
    """
    # L1
    mary_morning = 1 # Mary gave Luna 1 cup of kibble in the morning
    mary_evening = 1 # Mary gave Luna 1 cup of kibble in the evening
    mary_total = mary_morning + mary_evening

    # L2
    frank_afternoon = 1 # Frank gave Luna 1 cup of kibble in the afternoon
    frank_late_evening_multiplier = 2 # twice as much in the late evening as he had given Luna in the afternoon
    frank_late_evening = frank_afternoon * frank_late_evening_multiplier
    frank_total = frank_afternoon + frank_late_evening

    # L3
    total_fed = mary_total + frank_total

    # L4
    bag_start = 12 # new, 12-cup bag of kibble
    cups_remaining = bag_start - total_fed

    # FA
    answer = cups_remaining
    return answer