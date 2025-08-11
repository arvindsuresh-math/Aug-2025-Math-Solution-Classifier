def solve():
    """Index: 6181.
    Returns: the total number of pills left after filling the pillbox for two weeks.
    """
    # L1
    pills_per_bottle_120 = 120 # 120 pills in them each
    num_bottles_120_pills = 3 # 3 of the bottles
    total_pills_120_bottles = pills_per_bottle_120 * num_bottles_120_pills

    # L2
    pills_per_bottle_30 = 30 # 30 pills each
    num_bottles_30_pills = 2 # 2 of the bottles
    total_pills_30_bottles = pills_per_bottle_30 * num_bottles_30_pills

    # L3
    total_initial_pills = total_pills_120_bottles + total_pills_30_bottles

    # L4
    pillbox_days = 7 # 7-day pill box
    weeks_to_fill = 2 # for 2 weeks
    total_days_filled = pillbox_days * weeks_to_fill

    # L5
    num_supplements = 5 # 5 different supplements
    pills_per_day = 1 * num_supplements # one pill of each supplement
    pills_used = total_days_filled * pills_per_day

    # L6
    pills_left = total_initial_pills - pills_used

    # FA
    answer = pills_left
    return answer