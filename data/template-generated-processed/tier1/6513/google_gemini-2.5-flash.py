def solve():
    """Index: 6513.
    Returns: the number of fish Julio has after losing some.
    """
    # L1
    fish_per_hour = 7 # 7 fish every hour
    hours_fished = 9 # By the 9th hour
    total_fish_caught = fish_per_hour * hours_fished

    # L2
    fish_lost = 15 # loses 15 fish
    remaining_fish = total_fish_caught - fish_lost

    # FA
    answer = remaining_fish
    return answer