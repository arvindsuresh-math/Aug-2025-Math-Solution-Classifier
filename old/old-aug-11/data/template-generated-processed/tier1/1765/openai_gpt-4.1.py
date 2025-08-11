def solve():
    """Index: 1765.
    Returns: the number of worms mama bird still needs to catch to feed her babies for 3 days.
    """
    # L1
    num_babies = 6 # 6 babies in the nest
    worms_per_baby_per_day = 3 # feed each baby 3 worms a day
    daily_worms_needed = num_babies * worms_per_baby_per_day

    # L2
    num_days = 3 # feed them for 3 days
    total_worms_needed = daily_worms_needed * num_days

    # L3
    mama_caught = 13 # she caught 13 worms
    worms_stolen = 2 # had 2 stolen
    mama_worms_left = mama_caught - worms_stolen

    # L4
    papa_caught = 9 # Papa bird caught 9 worms
    total_worms_have = mama_worms_left + papa_caught

    # L5
    worms_still_needed = total_worms_needed - total_worms_have

    # FA
    answer = worms_still_needed
    return answer