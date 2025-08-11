def solve():
    """Index: 6978.
    Returns: the number of deer each hunting wolf needs to kill.
    """
    # L1
    hunting_wolves = 4 # 4 wolves out hunting
    additional_wolves = 16 # 16 additional wolves
    total_wolves = hunting_wolves + additional_wolves

    # L2
    meat_per_wolf_per_day = 8 # Each wolf needs to eat 8 pounds of meat a day
    daily_meat_needed = total_wolves * meat_per_wolf_per_day

    # L3
    days_without_hunting = 5 # won't hunt again for five days
    total_meat_needed_for_period = days_without_hunting * daily_meat_needed

    # L4
    meat_per_deer = 200 # Each deer contains 200 pounds of meat
    total_deer_to_kill = total_meat_needed_for_period / meat_per_deer

    # L5
    deer_per_hunting_wolf = total_deer_to_kill / hunting_wolves

    # FA
    answer = deer_per_hunting_wolf
    return answer