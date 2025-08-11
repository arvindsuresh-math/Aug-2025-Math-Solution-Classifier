def solve():
    """Index: 6314.
    Returns: the difference between ripe and unripe peaches after five days.
    """
    # L1
    ripen_per_day = 2 # two more ripen every day
    days = 5 # after five days
    peaches_ripened_over_days = ripen_per_day * days

    # L2 (Implicit calculation, not a separate logical step)
    initial_ripe_peaches = 4 # Four of the peaches are ripe
    total_ripened_before_eaten = peaches_ripened_over_days + initial_ripe_peaches

    # L3
    eaten_on_third_day = 3 # three are eaten
    ripe_peaches_left = total_ripened_before_eaten - eaten_on_third_day

    # L4
    total_peaches_in_bowl = 18 # A bowl of fruit holds 18 peaches
    unripe_peaches_left = total_peaches_in_bowl - total_ripened_before_eaten

    # L5
    difference_ripe_unripe = ripe_peaches_left - unripe_peaches_left

    # FA
    answer = difference_ripe_unripe
    return answer