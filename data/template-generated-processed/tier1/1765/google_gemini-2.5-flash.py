def solve():
    """Index: 1765.
    Returns: the number of worms Mama bird still needs to catch.
    """
    # L1
    num_babies = 6 # 6 babies in the nest
    worms_per_baby_per_day = 3 # feed each baby 3 worms a day
    worms_needed_per_day = num_babies * worms_per_baby_per_day

    # L2
    num_days_to_feed = 3 # feed them for 3 days
    total_worms_needed = worms_needed_per_day * num_days_to_feed

    # L3
    mama_caught_initial = 13 # she caught 13 worms
    worms_stolen = 2 # had 2 stolen
    mama_worms_after_stolen = mama_caught_initial - worms_stolen

    # L4
    papa_worms = 9 # Papa bird caught 9 worms
    total_worms_available = mama_worms_after_stolen + papa_worms

    # L5
    worms_still_needed = total_worms_needed - total_worms_available

    # FA
    answer = worms_still_needed
    return answer